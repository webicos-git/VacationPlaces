# Generated by Django 3.2.7 on 2022-06-09 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotels', '0003_auto_20220609_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotels',
            name='id',
            field=models.AutoField(default='', primary_key=True, serialize=False),
        ),
    ]
