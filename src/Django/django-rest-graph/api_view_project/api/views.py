from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class ItemView(APIView):
    def get(self, request):
        return Response({'message': 'This is a GET request'})
    
    def post(self, request):
        return Response({'message': 'This is a POST request'})
    
    def put(self, request):
        return Response({'message': 'This is a PUT request'})
    
    def delete(self, request):
        return Response({'message': 'This is a DELETE request'})
    
    def patch(self, request):
        return Response({'message': 'This is a PATCH request'})