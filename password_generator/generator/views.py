from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'generator/home.html',{'anykey' : 'anyvalue'})

def mypage(request):
    return HttpResponse("<h1>welcome to mypage!</h1>")