# Generated by Django 3.2.6 on 2021-08-22 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geography', '0010_alter_gps_elevation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectingtrip',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]