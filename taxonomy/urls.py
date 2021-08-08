from rest_framework import routers
from django.urls import path
from django.conf.urls import include
from taxonomy import views

router = routers.DefaultRouter()

urlpatterns = [
    path('api/taxonomy', include(router.urls)),
    path('api/taxonomy/orders', views.OrderList.as_view()),
    path('api/taxonomy/families', views.FamilyList.as_view()),
    path('api/taxonomy/subfamilies', views.SubfamilyList.as_view()),
    path('api/taxonomy/tribes', views.TribeList.as_view()),
    path('api/taxonomy/genera', views.GenusList.as_view()),
    path('api/taxonomy/species', views.SpeciesList.as_view()),
    path('api/taxonomy/subspecies', views.SubspeciesList.as_view())
]