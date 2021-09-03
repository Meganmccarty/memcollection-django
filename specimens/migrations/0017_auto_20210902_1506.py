# Generated by Django 3.2.6 on 2021-09-02 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('specimens', '0016_alter_specimenrecord_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specimenrecord',
            name='determined_year',
            field=models.IntegerField(blank=True, help_text='Enter the year the determination was made', null=True),
        ),
        migrations.AlterField(
            model_name='specimenrecord',
            name='determiner',
            field=models.ForeignKey(blank=True, help_text='Select the person who determined the specimen', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='specimen_determiners', to='specimens.person'),
        ),
    ]
