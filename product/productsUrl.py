
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.productFunction),
    path('date', views.date),
]