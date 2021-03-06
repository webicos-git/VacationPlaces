# Generated by Django 3.2.7 on 2022-06-09 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('bedroomsAvailable', models.CharField(max_length=100)),
                ('facilitiesAvailable', models.CharField(choices=[('Wifi', 'WIFI'), ('coffee', 'Coffee'), ('breakfast', 'Breakfast'), ('ac rooms', 'Ac rooms'), ('water', 'Water'), ('clean & sanitized rooms', 'Clean & sanitized rooms'), ('pick up', 'Pick up'), ('swimming pool', 'Swimming pool'), ('barbeque', 'Barbeque'), ('garden', 'Garden'), ('parking', 'Parking')], max_length=100)),
                ('mainImage', models.ImageField(blank=True, null=True, upload_to='mainImages/')),
                ('whatsappNumber', models.CharField(max_length=100)),
                ('callNumber', models.CharField(max_length=100)),
                ('pricingStarAt', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('whatToExpect', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='hotelimages/')),
                ('note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hotels.hotels')),
            ],
        ),
    ]
