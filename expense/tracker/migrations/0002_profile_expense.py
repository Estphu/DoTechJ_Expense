# Generated by Django 4.2.5 on 2023-09-23 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='expense',
            field=models.FloatField(default=0),
        ),
    ]
