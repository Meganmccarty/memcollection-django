# Generated by Django 3.2.6 on 2021-12-26 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0005_auto_20210904_1840'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='insectimage',
            options={'ordering': ['-date', 'name']},
        ),
    ]
