# Generated by Django 3.2.7 on 2022-06-11 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hotels', '0006_contactus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='messages',
            new_name='message',
        ),
    ]
