# Generated by Django 3.2.6 on 2022-04-20 09:55

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_alter_speciespage_distribution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speciespage',
            name='seasonality',
            field=ckeditor.fields.RichTextField(blank=True, default='', help_text='Enter seasonality details'),
        ),
    ]
