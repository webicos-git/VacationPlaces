# Generated by Django 3.2.7 on 2022-06-11 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotels', '0005_alter_hotels_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=500)),
                ('messages', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
