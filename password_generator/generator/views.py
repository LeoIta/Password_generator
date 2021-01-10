from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello dear friend!")

def mypage(request):
    return HttpResponse("<h1>welcome to mypage!</h1>")