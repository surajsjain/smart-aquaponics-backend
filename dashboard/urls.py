from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.mainBoard),
    path('greenshouses/', views.warehouseDisplay),
    path('greenshouses/<int:wnum>/', views.warehouseSpecificDisplay),
    # path('temperature/', views.sysDetails),
    path('plants/', views.allPlants),
    path('plants/<int:pid>/', views.plantDetails)
]
