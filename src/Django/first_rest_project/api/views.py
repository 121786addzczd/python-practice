from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime, timezone
import pytz


def index(request):
    return HttpResponse('<h1>Hello World</h1>')
    # return JsonResponse({'page' : 'Hello World'})
    
    
# 時間を返す
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def country_datetime(request):
    if request.method == 'POST':
        # print(request.data)
        requested_timezone = request.data.get('timezone')
        if requested_timezone:
            tz = pytz.timezone(requested_timezone)
            utc_datetime = datetime.now(timezone.utc)
            return Response({f"DateTime POST: {requested_timezone}": utc_datetime.astimezone(tz)})
    elif request.method == 'PUT':
        print('PUTが呼ばれました')
    elif request.method == 'DELETE':
        print('DELETEが呼ばれました')
    else:
        """
        以下URLを直入力して取得する値が時間にあったものになるか確認
        - http://localhost:8000/api/country_datetime/?timezone=Asia/Tokyo
        - http://localhost:8000/api/country_datetime/?timezone=US/Eastern
        - http://localhost:8000/api/country_datetime/?timezone=US/Pacific
        """
        requested_timezone = request.query_params.get('timezone')
        if requested_timezone:
            tz = pytz.timezone(requested_timezone)
            utc_datetime = datetime.now(timezone.utc)
            return Response({f"DateTime GET: {requested_timezone}": utc_datetime.astimezone(tz)})
    return Response({"Datetime": datetime.now()})