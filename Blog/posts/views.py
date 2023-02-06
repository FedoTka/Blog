from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    n = {'Vlad', 'Kirill', 'Mark', 'artem', 'Igor'}
    return render(request, 'posts/index.html', context={'names' :n })