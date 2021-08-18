from django.urls import path
from pages import views

urlpatterns = [
    path('species-pages/', views.SpeciesPageList.as_view())
]