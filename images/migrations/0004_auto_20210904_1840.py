# Generated by Django 3.2.6 on 2021-09-04 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_auto_20210904_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habitatimage',
            name='date',
            field=models.DateField(help_text='Enter the date and time the image was taken'),
        ),
        migrations.AlterField(
            model_name='insectimage',
            name='date',
            field=models.DateField(help_text='Enter the date and time the image was taken'),
        ),
        migrations.AlterField(
            model_name='plantimage',
            name='date',
            field=models.DateField(help_text='Enter the date and time the image was taken'),
        ),
    ]
