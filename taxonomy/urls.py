from django.urls import path
from taxonomy import views

urlpatterns = [
    path('orders/', views.OrderList.as_view()),
    path('families/', views.FamilyList.as_view()),
    path('subfamilies/', views.SubfamilyList.as_view()),
    path('tribes/', views.TribeList.as_view()),
    path('genera/', views.GenusList.as_view()),
    path('species/', views.SpeciesList.as_view()),
    path('subspecies/', views.SubspeciesList.as_view())
]