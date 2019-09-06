from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http import HttpResponseRedirect
from systems.models import *
# Create your views here.

def mainBoard(request):
    warehouses = Warehouse.objects.all()
    plants = Plant.objects.all()
    ctxt = {
        'warehouses' : warehouses,
        'plants' : plants
    }
    return render(request, 'dashboard/dashHome.html', context=ctxt)

# def sysDetails(request):
#     return render(request, 'dashboard/temperaturePage.html')

def plantDetails(request, pid):
    plant = Plant.objects.filter(id = pid)
    ctxt = {
        'plant' : plant
    }
    return render(request, 'dashboard/plantDetPage.html', context=ctxt)

def warehouseSpecificDisplay(request, wnum):
    w = Warehouse.objects.filter(id = wnum)
    w = w[0]
    plants = Plant.objects.filter(Warehouse = w.id)
    ctxt = {
        'plants' : plants,
        'warehouse' :  w
    }
    # print(ctxt)
    return render(request, 'dashboard/greenhouseDash.html', context=ctxt)

def warehouseDisplay(request):
    warehouses = Warehouse.objects.all()
    ctxt = {
        'warehouses' : warehouses,
    }
    # return render(request, 'dashboard/dashHome.html', context=ctxt)
    return render(request, 'dashboard/allGreenhouses.html', context = ctxt)

def allPlants(request):
    plants = Plant.objects.all()
    ctxt = {
        'plants' : plants,
    }
    # print(ctxt)
    return render(request, 'dashboard/allPlants.html', context=ctxt)
