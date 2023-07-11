from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def date(reqest):
    return HttpResponse('this is product date function')

def productFunction(request):
    name = 'Pradipta'
    age  = 12
    data = {'name': name, 'age':age}
    return render(request, 'products/index.html', data)
