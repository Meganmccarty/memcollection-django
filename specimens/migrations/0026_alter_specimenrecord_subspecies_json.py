# Generated by Django 3.2.6 on 2022-03-19 15:59

import django.core.serializers.json
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specimens', '0025_specimenrecord_subspecies_json'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specimenrecord',
            name='subspecies_json',
            field=models.JSONField(default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder),
        ),
    ]