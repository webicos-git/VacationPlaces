from django.shortcuts import render
from .models import Hotels, Images, ContactUs
# Create your views here.


def index(request):
    hotels = Hotels.objects.all().values()
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
    hotels = Hotels.objects.all().values()
    print(type(hotel))
    myDict = {
        'hotel': hotel,
        'hotels': hotels
    }
    return render(request, 'single-hotel.html', myDict)


def contact(request):
    if request.method == 'POST':
        print(request.POST)
        data = request.POST
        contactUs = ContactUs(
            name=data['name'], email=data['email'], message=data['text'])
        contactUs.save()
        return render(request, 'index.html', {'message': "Form Submitted Successfully"})
    return render(request, 'contact.html')
