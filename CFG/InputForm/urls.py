from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('/addcomplaint', views.addcomplaint,  name ="Addcomplaint"), 

]