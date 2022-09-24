from django.urls import path
from . import views
import dkSVProgram
import re


#urlConfig
urlpatterns = [
    path('members', views.say_hello, name= "say_hello"),
    path('add/', views.add, name='add'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
    path('Quary/', views.Quary, name='Quary'),
    path('Quary/QuaryResp/', views.QuaryResp, name='QuaryResp'),
]
