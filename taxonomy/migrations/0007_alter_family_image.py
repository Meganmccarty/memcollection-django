# Generated by Django 3.2.6 on 2021-11-18 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxonomy', '0006_alter_family_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family',
            name='image',
            field=models.FileField(upload_to='insect-photos'),
        ),
    ]