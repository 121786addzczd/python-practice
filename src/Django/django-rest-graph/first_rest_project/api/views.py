from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime, timezone
import pytz
from pytz.exceptions import UnknownTimeZoneError
from rest_framework import status

def index(request):
    # return HttpResponse("<h1>Hello, this is the API index page.</h1>") # HTML response
    return JsonResponse({"message": "Hello, json"}) # JSON response

# 時間を返す
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def country_datetime(request):
    print(f"RequestMethod={request.method}")
    if request.method == 'POST':
        print(f"RequestBody={request.data}")
        requested_timezone = request.data.get('timezone')
        if requested_timezone:
            try:
                tz = pytz.timezone(requested_timezone)
            except UnknownTimeZoneError:
                return Response(
                    {"error POST": "Timezone not exists"}, status=status.HTTP_400_BAD_REQUEST
                )
            utc_datetime = datetime.now(timezone.utc)
            return Response(
                {f"DateTime POST: {requested_timezone}": utc_datetime.astimezone(tz)}
            )
    elif request.method == 'PUT':
        print('PUTが呼ばれました')
    elif request.method == 'DELETE':
        print('DELETEが呼ばれました')
    else:
        requested_timezone = request.query_params.get('timezone')
        if requested_timezone:
            try:
                tz = pytz.timezone(requested_timezone)
            except UnknownTimeZoneError:
                # http://127.0.0.1:8000/api/country_datetime/?timezone=US/Easter といった不正なtimezone値の時
                return Response(
                    {"error GET": "Timezone not exists"}, status=status.HTTP_400_BAD_REQUEST
                )
            utc_datetime = datetime.now(timezone.utc)
            return Response(
                {f"DateTime GET: {requested_timezone}": utc_datetime.astimezone(tz)}
            )
    return Response({"DateTime": datetime.now()})