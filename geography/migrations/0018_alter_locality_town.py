# Generated by Django 3.2.6 on 2022-01-17 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geography', '0017_alter_locality_range'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locality',
            name='town',
            field=models.CharField(blank=True, default='', help_text='Enter the nearest town', max_length=50),
        ),
    ]
