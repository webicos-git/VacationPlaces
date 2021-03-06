"""VacationPlaces URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Hotels import views
from django.conf import settings

from django.conf.urls.static import static

admin.site.site_header = "Vacation Places"
admin.site.site_title = "Vacation Places Admin"
admin.site.index_title = "Welcome to Vacation Places Portal"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('hotels', views.hotelListing),
    path('contact', views.contact),
    path('hotelSingle/<str:id>/', views.hotelSingle,name='hotelSingle'),
    path('privacy-policy', views.privacyPolicy),
    path('terms-and-conditions', views.termsAndCondition),
    path('privacy-statement', views.privacyStatement),
    path('about-us', views.aboutUs)
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
