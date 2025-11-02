from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime, timezone
import pytz

def index(request):
    # return HttpResponse("<h1>Hello, this is the API index page.</h1>") # HTML response
    return JsonResponse({"message": "Hello, json"}) # JSON response

# 時間を返す
@api_view(['GET', 'POST'])
def country_datetime(request):
    print(f"RequestMethod={request.method}")
    if request.method == 'POST':
        print(f"RequestBody={request.data}")
        requested_timezone = request.data.get('timezone')
        if requested_timezone:
            tz = pytz.timezone(requested_timezone)
            utc_datetime = datetime.now(timezone.utc)
            return Response(
                {f"DateTime POST: {requested_timezone}": utc_datetime.astimezone(tz)}
            )
    else:
        requested_timezone = request.query_params.get('timezone')
        if requested_timezone:
            tz = pytz.timezone(requested_timezone)
            utc_datetime = datetime.now(timezone.utc)
            return Response(
                {f"DateTime GET: {requested_timezone}": utc_datetime.astimezone(tz)}
            )
    return Response({"DateTime": datetime.now()})