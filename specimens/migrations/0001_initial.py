# Generated by Django 3.2.6 on 2021-08-11 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text="Enter the person's first name", max_length=50)),
                ('middle_initial', models.CharField(blank=True, help_text="Enter the person's middle initial", max_length=1)),
                ('last_name', models.CharField(help_text="Enter the person's last name", max_length=1)),
                ('suffix', models.CharField(blank=True, help_text='Enter a suffix, if the person has one', max_length=5)),
            ],
            options={
                'verbose_name_plural': 'People',
                'ordering': ['last_name'],
            },
        ),
    ]
