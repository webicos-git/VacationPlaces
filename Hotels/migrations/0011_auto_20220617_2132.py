# Generated by Django 3.2.7 on 2022-06-17 16:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotels', '0010_auto_20220617_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotels',
            name='iframe',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='hotels',
            name='ratings',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 17, 21, 32, 15, 753370)),
        ),
        migrations.AlterField(
            model_name='search',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 17, 21, 32, 15, 753370)),
        ),
    ]
