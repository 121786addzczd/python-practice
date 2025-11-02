from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime

def index(request):
    # return HttpResponse("<h1>Hello, this is the API index page.</h1>") # HTML response
    return JsonResponse({"message": "Hello, json"}) # JSON response

# 時間を返す
@api_view(['GET'])
def country_datetime(request):
    return Response({"DateTime": datetime.now()})