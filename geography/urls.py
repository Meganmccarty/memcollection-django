from django.urls import path
from geography import views

urlpatterns = [
    path('countries/', views.CountryList.as_view()),
    path('states/', views.StateList.as_view()),
    path('counties/', views.CountyList.as_view()),
    path('localities/', views.LocalityList.as_view()),
    path('places-collected/', views.GPSList.as_view()),
    path('collecting-trips/', views.CollectingTripList.as_view())
]