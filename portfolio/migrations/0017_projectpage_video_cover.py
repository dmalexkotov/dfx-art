# Generated by Django 3.0.9 on 2020-10-16 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('portfolio', '0016_auto_20200923_0251'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectpage',
            name='video_cover',
            field=models.ForeignKey(blank=True, help_text='The image for placeholding the video', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
