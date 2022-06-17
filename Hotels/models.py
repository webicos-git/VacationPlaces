from django.db import models

# Create your models here.
import datetime


class Hotels(models.Model):
    name = models.CharField(max_length=500)
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    bedroomsAvailable = models.CharField(max_length=100)
    WIFI = models.BooleanField(default=False)
    SwimmingPool = models.BooleanField(default=False)
    Garden = models.BooleanField(default=False)
    Breakfast = models.BooleanField(default=False)
    ACRooms = models.BooleanField(default=False)
    CleanAndSanitised = models.BooleanField(default=False)
    Barbecue = models.BooleanField(default=False)
    Parking = models.BooleanField(default=False)
    Kitchen = models.BooleanField(default=False)
    GeyserOrHotWater = models.BooleanField(default=False)
    CommodeWestern = models.BooleanField(default=False)
    CommodeIndian = models.BooleanField(default=False)
    BarORDrinks = models.BooleanField(default=False)
    Pets = models.BooleanField(default=False)
    Drinks = models.BooleanField(default=False)
    Party = models.BooleanField(default=False)
    LoudMusic = models.BooleanField(default=False)
    LateNightParty = models.BooleanField(default=False)
    PoolParty = models.BooleanField(default=False)
    ColoursInFestival = models.BooleanField(default=False)
    OutsideFoodAllowed = models.BooleanField(default=False)
    FrontDesk = models.BooleanField(default=False)
    cleaner = models.BooleanField(default=False)
    CareTaker = models.BooleanField(default=False)
    Pickup = models.BooleanField(default=False)
    FoodOrder = models.BooleanField(default=False)
    # garden = models.BooleanField(default=False)

    mainImage = models.ImageField(
        upload_to='mainImages/', null=True, blank=True)
    whatsappNumber = models.CharField(max_length=100)
    callNumber = models.CharField(max_length=100)
    pricingStarAt = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    whatToExpect = models.TextField()
    def __str__(self):
        return self.name


class Images(models.Model):
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='hotelimages/', null=True, blank=True)
    def __str__(self):
        return self.hotel.name


class ContactUs(models.Model):
    name = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    message = models.TextField()
    date = date = models.DateTimeField(
        default=datetime.datetime.now(), blank=True)

    def __str__(self):
        return self.name
