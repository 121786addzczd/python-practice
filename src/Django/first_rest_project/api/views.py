from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def index(request):
    return HttpResponse('<h1>Hello World</h1>')
    # return JsonResponse({'page' : 'Hello World'})