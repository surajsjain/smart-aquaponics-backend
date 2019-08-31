from django.urls import path, include
from . import views

app_name = 'conditions'

urlpatterns = [
    path('plant', views.plant_list),
]
