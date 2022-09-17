from django.urls import path
from . import views
import dkSVProgram
import re


#urlConfig
urlpatterns = [
    path('members', views.say_hello),
    path('members/add', views.say_add),
    path('members/add/addrecord/', views.addrecord),
]
