from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Members
#from SqlTest import sqlTest

def say_hello(request):
    mymembers = Members.objects.all().values()
    template = loader.get_template('hello.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def add(request):
    #return HttpResponse("hello world")
    return render(request, 'add.html')

def addrecord(request):
    x = request.POST['Phone']
    y = request.POST['Timeline']
    member = Members(PhoneNum=x, Timeline=y)
    member.save()
    return HttpResponseRedirect(reverse('say_hello'))

def Quary(request):
    #return HttpResponse("hello world")
    return render(request, 'Qrequest.html')

def QuaryResp(request):
    mymembers = Members.objects.all().values()
    template = loader.get_template('Qrespond.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))
