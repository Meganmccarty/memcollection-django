# Generated by Django 3.2.6 on 2022-04-20 09:55

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_alter_speciespage_food'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speciespage',
            name='life_cycle',
            field=ckeditor.fields.RichTextField(blank=True, default='', help_text='Enter details about the life cycle'),
        ),
    ]
