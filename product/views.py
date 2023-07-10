from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def date(reqest):
    return HttpResponse('this is product date function')

def productFunction(request):
    return render(request, 'products/index.html')
