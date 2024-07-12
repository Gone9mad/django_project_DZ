from django.shortcuts import render

from django.shortcuts import render

def home(request):
    return render(request, 'catalog/home.html')

def contacts(request):
    return render(request, 'catalog/contacts.html')
