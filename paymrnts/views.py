from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse ('Pradipta first Django')


def paymentFunction(request):
    a = 'this is payment page'
    return HttpResponse(f'hi {a}')

def calculateFunction(request):
    a= 3
    b = 4
    c = a+b
    return HttpResponse(f'The result is {c}. do again')

def firstFunction(req):
    return render(req, 'payment/index.html')