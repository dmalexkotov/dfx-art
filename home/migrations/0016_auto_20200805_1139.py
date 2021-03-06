# Generated by Django 3.0.8 on 2020-08-05 11:39

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20200805_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=wagtail.core.fields.StreamField([('main', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add title', required=True)), ('text', wagtail.core.blocks.TextBlock(help_text='Add text', required=True)), ('background', wagtail.documents.blocks.DocumentChooserBlock(help_text='Add background image or video', required=True))])), ('about', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add title', required=True)), ('sub_title', wagtail.core.blocks.CharBlock(help_text='Add subtitle', required=False)), ('text', wagtail.core.blocks.RichTextBlock(help_text='Add text', required=True)), ('video_background', wagtail.documents.blocks.DocumentChooserBlock(help_text='Add background video', required=False)), ('image_background', wagtail.images.blocks.ImageChooserBlock(help_text='Add background image', required=False)), ('side', wagtail.core.blocks.BooleanBlock(help_text='Flip side', required=False))])), ('about_list', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add title', required=True)), ('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add title', required=True)), ('sub_title', wagtail.core.blocks.CharBlock(help_text='Add subtitle', required=False)), ('text', wagtail.core.blocks.RichTextBlock(help_text='Add text', required=True)), ('video_background', wagtail.documents.blocks.DocumentChooserBlock(help_text='Add background video', required=False)), ('image_background', wagtail.images.blocks.ImageChooserBlock(help_text='Add background image', required=False)), ('side', wagtail.core.blocks.BooleanBlock(help_text='Flip side', required=False))])))])), ('projects_list', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add title', required=True)), ('content', wagtail.core.blocks.ListBlock(wagtail.core.blocks.PageChooserBlock(page_type=['portfolio.ProjectPage'])))])), ('informers', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock(help_text='Add text', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Add background image', required=True))])))])), ('programming', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add title', required=True)), ('description', wagtail.core.blocks.RichTextBlock(help_text='Description', required=False)), ('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('description', wagtail.core.blocks.TextBlock())])))])), ('awargs', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add title', required=True)), ('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('badge', wagtail.images.blocks.ImageChooserBlock()), ('description', wagtail.core.blocks.TextBlock())])))])), ('founders_patents', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add title', required=True)), ('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('desc_title', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.images.blocks.ImageChooserBlock()), ('description', wagtail.core.blocks.TextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('image_text', wagtail.core.blocks.CharBlock())])))])), ('history', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add title', required=True)), ('content', wagtail.core.blocks.RichTextBlock())]))]),
        ),
    ]
