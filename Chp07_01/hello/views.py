from django.shortcuts import render
from django.http import HttpResponse

def sayHello(request, name):
    myHtml = f'<h1>Hello, {name} !</h1>'
    return HttpResponse(myHtml)
