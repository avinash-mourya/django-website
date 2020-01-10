from django.shortcuts import render
from django.http import *
def index(request):
    return render(request,'index.html')

def camera(request):
    return render(request,"camera.html")