from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request,'generator/home.html')

def password(request):
    
    
    characters = list('abcdefghijklmnopqrstuvwxyz')

    length = int(request.GET.get('length',default=12))

    my_password = ''

    for char in range(length):
        my_password += random.choice(characters)

    return  render(request,'generator/password.html',{'password':my_password})
