# Generated by Django 3.0.2 on 2020-01-21 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
    ]
