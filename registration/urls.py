from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='registration') #name=name of template
]