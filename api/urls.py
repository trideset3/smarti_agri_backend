from django.urls import path
from . import views


urlpatterns = [
     path('getFields/', views.getFields, name='getFields'),
     path('getSeasons/', views.getSeasons, name='getSeasons'),
     path('getFieldDetails/', views.getFieldDetails, name='getFieldDetails'),
 ]
