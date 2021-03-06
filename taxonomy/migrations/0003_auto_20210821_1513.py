# Generated by Django 3.2.6 on 2021-08-21 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxonomy', '0002_auto_20210807_2253'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='family',
            options={'ordering': ['name'], 'verbose_name_plural': 'Families'},
        ),
        migrations.AlterModelOptions(
            name='genus',
            options={'ordering': ['name'], 'verbose_name_plural': 'Genera'},
        ),
        migrations.AlterModelOptions(
            name='species',
            options={'ordering': ['name'], 'verbose_name_plural': 'Species'},
        ),
        migrations.AlterModelOptions(
            name='subfamily',
            options={'ordering': ['name'], 'verbose_name_plural': 'Subfamilies'},
        ),
        migrations.AlterModelOptions(
            name='subspecies',
            options={'ordering': ['name'], 'verbose_name_plural': 'Subspecies'},
        ),
    ]
