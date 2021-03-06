# Generated by Django 3.2.6 on 2021-08-12 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specimens', '0004_specimenrecord_collector'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specimenrecord',
            name='sex',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female'), ('unknown', 'unknown')], default='unknown', help_text="Select the specimen's sex", max_length=10),
        ),
    ]
