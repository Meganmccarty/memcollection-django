# Generated by Django 3.2.6 on 2021-08-24 15:50

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('specimens', '0014_alter_specimenrecordimage_usi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specimenrecord',
            name='habitat',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Enter habitat details where the specimen was collected', null=True),
        ),
        migrations.AlterField(
            model_name='specimenrecord',
            name='notes',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Enter any other notes about the specimen', null=True),
        ),
    ]
