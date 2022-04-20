# Generated by Django 3.2.6 on 2022-04-20 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specimens', '0034_alter_specimenrecord_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specimenrecord',
            name='weather',
            field=models.CharField(blank=True, default='', help_text="Enter the weather conditions during the specimen's collection", max_length=100),
        ),
    ]
