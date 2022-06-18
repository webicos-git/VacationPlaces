# Generated by Django 4.0.5 on 2022-06-18 11:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotels', '0014_auto_20220617_2132'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotels',
            old_name='iframe',
            new_name='mapLink',
        ),
        migrations.AlterField(
            model_name='contactus',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 18, 17, 19, 45, 928447)),
        ),
        migrations.AlterField(
            model_name='search',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 18, 17, 19, 45, 929448)),
        ),
    ]
