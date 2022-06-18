from django.shortcuts import render, redirect
from .models import Hotels, Images, ContactUs, Search
# Create your views here.


def index(request):
    hotels = Hotels.objects.all().values()

    if request.method == 'POST':
        print(request.POST)
        data = request.POST
        search = Search(destination=data['destination'],
                        checkInCheckOut=data['checkincheckout'], rooms=data['rooms'])
        search.save()

        final = []
        rooms = []

        for hotel in hotels:
            if int(hotel['bedroomsAvailable']) >= int(data['rooms']):
                rooms.append(hotel)

        for hotel in rooms:
            name = hotel['name']
            if data['destination'].lower() in name.lower() or data['destination'].lower() in hotel['location'].lower():
                final.append(hotel)

        myDict = {
            'hotels': final,
            'total': len(final),
        }
        request.session['resp'] = myDict
        return redirect('/hotels')

    return render(request, 'index.html')


def hotelListing(request):
    hotels = Hotels.objects.all().values()
    response1 = request.session['resp']
    # print("response=",response1)
    if response1 is not None:
        request.session['resp'] = None
        return render(request, 'hotel-listing.html', response1)

    if request.method == 'POST':
        print(request.POST)
        data = request.POST
        search = Search(destination=data['destination'],
                        checkInCheckOut=data['checkincheckout'], rooms=data['rooms'])
        search.save()

        final = []
        rooms = []

        for hotel in hotels:
            if int(hotel['bedroomsAvailable']) >= int(data['rooms']):
                rooms.append(hotel)

        for hotel in rooms:
            name = hotel['name']
            if data['destination'].lower() in name.lower() or data['destination'].lower() in hotel['location'].lower():
                final.append(hotel)

        myDict = {
            'hotels': final,
            'total': len(final),
        }
        return render(request, 'hotel-listing.html', myDict)

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
