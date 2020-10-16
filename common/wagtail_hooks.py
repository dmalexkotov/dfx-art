from wagtail.core import hooks
from wagtail.images import image_operations

from django.conf import settings
from willow.plugins.pillow import PillowImage

from wagtail.images.image_operations import Operation
from PIL import Image


class WatermarkedOperation(Operation):
    # assumes an image in directory /app/static/watermark/
    watermark_path = settings.STATIC_ROOT + '/img/WaterLogo.png'

    opacity = 0.5

    def run(self, willow, image, env):
        # willow is the instance of the source image loaded into willow
        # image is the wagtail image representation which has methods like image.get_focal_point()
        # env contains additional info about the execution environment. 
        # simple transforms can be made by adding to env, such as jpeg_quality

        watermark = Image.open(self.watermark_path).convert("RGBA")

        wm_width, wm_height = watermark.size
        source_width, source_height = willow.get_size()

        wm_ratio = wm_width/wm_height
        target_wm_width = source_width / 3.5
        target_wm_height = target_wm_width/wm_ratio

        wm_offset = int(source_width * 0.03)

        # watermark = watermark.resize((int(target_wm_width), int(target_wm_height)), Image.LANCZOS)

        offset_x = (source_width - watermark.size[0]) - wm_offset
        offset_y = (source_height - watermark.size[1]) - wm_offset

        manipulated_image = Image.new('RGBA', (source_width, source_height), (255, 255, 255, 1))
        manipulated_image.paste(willow.get_pillow_image(), (0,0))
        manipulated_image.paste(watermark, (offset_x, offset_y), watermark)

        return PillowImage(manipulated_image)

    def construct(self):
        pass


@hooks.register('register_image_operations')
def register_custom_image_operations():
    return [
        ('watermark', WatermarkedOperation),
    ]