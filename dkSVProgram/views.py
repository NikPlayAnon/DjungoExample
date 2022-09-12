from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from SqlTest import sqlTest

def say_hello(request):
    #return HttpResponse("hello world")
    return render(request, 'hello.html', {'name':'Claus'})

def say_add(request):
    #return HttpResponse("hello world")
    return render(request, 'add.html')

def addrecord(request):
  x = request.POST['phone']
  y = request.POST['timeline']
  sqlTest.addToM(phoneNum=x, timeline=y)
  #member = Members(firstname=x, lastname=y)
  #member.save()
  #return HttpResponseRedirect(reverse('index'))