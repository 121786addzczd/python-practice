from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def index(request):
    # return HttpResponse("<h1>Hello, this is the API index page.</h1>") # HTML response
    return JsonResponse({"message": "Hello, json"}) # JSON response