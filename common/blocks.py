from wagtail.core import blocks


class ContactBlock(blocks.StructBlock):
    location = blocks.CharBlock(help_text='Add country', required=False)
    address = blocks.CharBlock(help_text='Add address', required=False)
    phone = blocks.CharBlock(help_text='Add phone', required=False)
    email = blocks.CharBlock(help_text='Add email', required=False)

    class Meta:
        template = 'common/blocks/contact_block.html'
        icon = 'plus'
        label = 'Contacts Block'