from wagtail.core import hooks

from django.conf import settings
from willow.plugins.pillow import PillowImage

from wagtail.images.image_operations import Operation
from PIL import Image

from common.models import SiteSettings


class WatermarkedOperation(Operation):
    # assumes an image in directory /app/static/watermark/
    watermark_logo_path = settings.STATIC_ROOT + '/img/WaterLogo.png'
    watermark_bg_path = settings.STATIC_ROOT + '/img/Watermark.png'

    opacity = 0.5

    def run(self, willow, image, env):
        # willow is the instance of the source image loaded into willow
        # image is the wagtail image representation which has methods like
        # image.get_focal_point()
        # env contains additional info about the execution environment. 
        # simple transforms can be made by adding to env, such as jpeg_quality

        source_width, source_height = willow.get_size()
        manipulated_image = Image.new(
            'RGBA',
            (source_width, source_height),
            (255, 255, 255, 1)
        )

        manipulated_image.paste(willow.get_pillow_image(), (0, 0))

        settings = SiteSettings.objects.all().first()

        if settings.watermark_logo:
            watermark_logo = Image.open(
                settings.watermark_logo.file.path
            ).convert("RGBA")

            wm_width, wm_height = watermark_logo.size

            # wm_ratio = wm_width/wm_height
            # target_wm_width = source_width / 3.5
            # target_wm_height = target_wm_width/wm_ratio

            wm_offset = int(source_width * 0.01)

            watermark_logo = watermark_logo.resize(
                (int(wm_width), int(wm_height)),
                Image.LANCZOS
            )

            offset_x = (source_width - watermark_logo.size[0]) - wm_offset
            offset_y = (source_height - watermark_logo.size[1]) - wm_offset

            manipulated_image.paste(
                watermark_logo, (offset_x, offset_y), watermark_logo
            )

        if settings.watermark_background:
            watermark_bg = Image.open(
                settings.watermark_background.file.path
            ).convert("RGBA")
            wm_bg_width, wm_bg_height = watermark_bg.size

            x_repeat = int(source_width / wm_bg_width) + 1
            y_repeat = int(source_height / wm_bg_height) + 1

            for x_index in range(x_repeat):
                for y_index in range(y_repeat):
                    manipulated_image.paste(
                        watermark_bg,
                        (x_index * wm_bg_width, y_index * wm_bg_height),
                        watermark_bg
                    )

        return PillowImage(manipulated_image)

    def construct(self, *args, **kwargs):
        pass


@hooks.register('register_image_operations')
def register_custom_image_operations():
    return [
        ('watermark', WatermarkedOperation),
    ]
