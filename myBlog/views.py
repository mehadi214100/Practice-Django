from django.http import HttpResponse
from django.shortcuts import render

def aboutus(request):
    return render(request,'aboutus.html')

def contactus(request):
    return render(request,'contactus.html')

def portfolio(request):
    return render(request,'portfolio.html')
