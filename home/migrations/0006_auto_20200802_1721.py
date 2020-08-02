# Generated by Django 3.0.8 on 2020-08-02 17:21

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20200802_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=wagtail.core.fields.StreamField([('banner', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add title', required=True)), ('text', wagtail.core.blocks.TextBlock(help_text='Add text', required=True)), ('background', wagtail.documents.blocks.DocumentChooserBlock(help_text='Add background image or video', required=True))])), ('about', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add title', required=True)), ('content', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add title', required=True)), ('text', wagtail.core.blocks.TextBlock(help_text='Add text', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Add background image', required=True))])))])), ('project_list', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add title', required=True)), ('content', wagtail.core.blocks.ListBlock(wagtail.core.blocks.PageChooserBlock(page_type=['portfolio.ProjectPage'])))])), ('informers', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add title', required=True)), ('content', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock(help_text='Add text', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Add background image', required=True))])))]))]),
        ),
    ]
