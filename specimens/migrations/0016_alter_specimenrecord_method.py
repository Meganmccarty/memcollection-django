# Generated by Django 3.2.6 on 2021-09-02 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specimens', '0015_auto_20210824_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specimenrecord',
            name='method',
            field=models.CharField(blank=True, choices=[('net', 'net'), ('reared', 'reared'), ('trap', 'trap'), ('UV trap', 'UV trap'), ('light', 'light'), ('MV light', 'MV light'), ('MV light sheet', 'MV light sheet'), ('UV light', 'UV light'), ('UV light sheet', 'UV light sheet'), ('UV/MV light sheet', 'UV/MV light sheet'), ('UV/MV/LED light sheet', 'UV/MV/LED light sheet'), ('bait', 'bait'), ('by hand', 'by hand'), ('sweep', 'sweep')], help_text='Select the method used to collected the specimen', max_length=50, null=True),
        ),
    ]
