# Generated by Django 3.0.8 on 2020-08-05 11:56

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectpage',
            name='description',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
    ]