from django.shortcuts import render
from .models import Hotels
# Create your views here.


def index(request):
    hotels = Hotels.objects.all().values()
    print(hotels)
    for h in hotels:
        print(h)

    return render(request, 'index.html')


def hotelListing(request):
    hotels = Hotels.objects.all().values()
    
    myDict = {
        'hotels': hotels,
        'total': len(hotels),
    }
    return render(request, 'hotel-listing.html', myDict)


def hotelSingle(request, id):
    hotel = Hotels.objects.all().get(id=id)
    print(type(hotel))
    myDict = {
        'hotel': hotel
    }
    return render(request, 'single-hotel.html', myDict)
