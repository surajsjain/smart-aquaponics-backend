from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http import HttpResponseRedirect
# Create your views here.

def mainBoard(request):
    return render(request, 'dashboard/dashHome.html')

def sysDetails(request):
    return render(request, 'dashboard/temperaturePage.html')
