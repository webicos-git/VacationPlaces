from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')

def hotelListing(request):
    return render(request, 'hotel-listing.html')

def hotelSingle(request):
    return render(request, 'single-hotel.html')
