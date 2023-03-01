
from django.shortcuts import render, redirect
from django.contrib import messages

def base(request):
    return render(request, 'base.html')
