# Generated by Django 3.2.6 on 2022-04-20 09:54

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_alter_speciespage_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speciespage',
            name='distribution',
            field=ckeditor.fields.RichTextField(blank=True, default='', help_text='Enter distribution details'),
        ),
    ]