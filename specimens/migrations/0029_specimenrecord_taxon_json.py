# Generated by Django 3.2.6 on 2022-03-20 13:13

import django.core.serializers.json
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specimens', '0028_auto_20220319_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='specimenrecord',
            name='taxon_json',
            field=models.JSONField(default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder),
        ),
    ]