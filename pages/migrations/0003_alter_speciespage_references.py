# Generated by Django 3.2.6 on 2021-09-03 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_alter_speciespage_references'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speciespage',
            name='references',
            field=models.ManyToManyField(blank=True, help_text='Enter citations used to write the info in the preciding fields', related_name='species_pages', to='pages.Reference'),
        ),
    ]
