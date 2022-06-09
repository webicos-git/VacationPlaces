# Generated by Django 3.2.7 on 2022-06-09 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotels', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='images',
            old_name='note',
            new_name='hotel',
        ),
        migrations.AddField(
            model_name='hotels',
            name='garden',
            field=models.BooleanField(default=False),
        ),
    ]
