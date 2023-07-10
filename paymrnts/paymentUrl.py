
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.firstFunction),
    path('payment', views.paymentFunction),
    path('calculate', views.calculateFunction),
]