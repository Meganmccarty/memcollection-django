from rest_framework import routers
from django.urls import path
from django.conf.urls import include
from geography import views

router = routers.DefaultRouter()

urlpatterns = [
    path('api/geography', include(router.urls)),
    path('api/geography/countries', views.CountryList.as_view()),
    path('api/geography/states', views.StateList.as_view()),
    path('api/geography/counties', views.CountyList.as_view()),
    path('api/geography/localities', views.LocalityList.as_view()),
    path('api/geography/gps-coordinates', views.GPSList.as_view()),
    path('api/geography/collecting-trips', views.CollectingTripList.as_view())
]