from django.shortcuts import render

def mainview(request):
    return render(request, 'index.html')
