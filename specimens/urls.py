from django.urls import path
from specimens import views

urlpatterns = [
    path('specimen-records/', views.SpecimenRecordList.as_view()),
    path('specimen-record-images/', views.SpecimenRecordImageList.as_view())
]