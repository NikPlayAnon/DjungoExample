from django.urls import path
from . import views
import dkSVProgram


#urlConfig
urlpatterns = [
    path('hello', views.say_hello)
]
