# Generated by Django 3.2.6 on 2021-08-09 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geography', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectingtrip',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='gps',
            name='latitude',
            field=models.DecimalField(decimal_places=8, help_text='Enter the latitude', max_digits=10),
        ),
        migrations.AlterField(
            model_name='gps',
            name='longitude',
            field=models.DecimalField(decimal_places=8, help_text='Enter the longitude', max_digits=11),
        ),
        migrations.AlterField(
            model_name='locality',
            name='country',
            field=models.ForeignKey(blank=True, help_text="Select the locality's country", null=True, on_delete=django.db.models.deletion.CASCADE, related_name='localities', to='geography.country'),
        ),
        migrations.AlterField(
            model_name='locality',
            name='county',
            field=models.ForeignKey(blank=True, help_text="Select the locality's county", null=True, on_delete=django.db.models.deletion.CASCADE, related_name='counties', to='geography.county'),
        ),
        migrations.AlterField(
            model_name='locality',
            name='range',
            field=models.CharField(blank=True, help_text='Enter the distance and direction of this locality from the nearest town', max_length=10),
        ),
        migrations.AlterField(
            model_name='locality',
            name='state',
            field=models.ForeignKey(blank=True, help_text="Select the locality's state", null=True, on_delete=django.db.models.deletion.CASCADE, related_name='states', to='geography.state'),
        ),
        migrations.AlterField(
            model_name='locality',
            name='town',
            field=models.CharField(blank=True, help_text='Enter the nearest town', max_length=50),
        ),
    ]
