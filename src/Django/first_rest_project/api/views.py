from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime


def index(request):
    return HttpResponse('<h1>Hello World</h1>')
    # return JsonResponse({'page' : 'Hello World'})
    
    
# 時間を返す
@api_view(['GET'])
def country_datetime(request):
    return Response({"Datetime": datetime.now()})