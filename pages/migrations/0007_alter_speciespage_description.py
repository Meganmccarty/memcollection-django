# Generated by Django 3.2.6 on 2022-04-20 09:54

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_alter_speciespage_taxonomy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speciespage',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, default='', help_text='Enter species description'),
        ),
    ]
