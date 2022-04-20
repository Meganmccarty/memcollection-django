# Generated by Django 3.2.6 on 2022-04-20 10:19

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('specimens', '0036_alter_specimenrecord_time_of_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specimenrecord',
            name='habitat',
            field=ckeditor.fields.RichTextField(blank=True, default='', help_text='Enter habitat details where the specimen was collected'),
        ),
    ]