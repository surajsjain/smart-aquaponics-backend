from django.urls import path, include
from . import views

app_name = 'systems'

urlpatterns = [
    path('warehouse/', views.warehouse_list),
]
