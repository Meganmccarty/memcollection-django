# Generated by Django 3.2.6 on 2022-04-20 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specimens', '0033_alter_specimenrecord_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specimenrecord',
            name='method',
            field=models.CharField(blank=True, choices=[('Net', 'Net'), ('Reared', 'Reared'), ('Trap', 'Trap'), ('UV trap', 'UV trap'), ('Light', 'Light'), ('MV light', 'MV light'), ('MV light sheet', 'MV light sheet'), ('UV light', 'UV light'), ('UV light sheet', 'UV light sheet'), ('UV/MV light sheet', 'UV/MV light sheet'), ('UV/MV/LED light sheet', 'UV/MV/LED light sheet'), ('Bait', 'Bait'), ('By hand', 'By hand'), ('Sweep', 'Sweep')], default='', help_text='Select the method used to collected the specimen', max_length=50),
        ),
    ]
