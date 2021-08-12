from django.urls import path
from specimens import views

urlpatterns = [
    path('specimen-records/', views.SpecimenRecordList.as_view())
]