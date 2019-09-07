from django.urls import path, include
from . import views

app_name = 'conditions'

urlpatterns = [
    path('plant', views.plant_list),
    path('pond', views.pond_list),
    path('watering', views.watering_list),
    path('fishfeed', views.fishfeeding_list),
    path('infocus/<int:pid>', views.focus),
    path('actuate/<int:pid>', views.actuate)
]
