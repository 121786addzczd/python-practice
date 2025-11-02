from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ItemsSerializer

class ItemView(APIView):
    def get(self, request):
        return Response({'message': 'This is a GET request'})
    
    def post(self, request):
        print(f"Request Data={request.data}")
        serializer = ItemsSerializer(data=request.data)
        print(serializer)

        # バリデーション
        print(serializer.is_valid(raise_exception=True))
        print(serializer.errors)
        return Response({'message': 'This is a POST request'})
    
    def put(self, request):
        return Response({'message': 'This is a PUT request'})
    
    def delete(self, request):
        return Response({'message': 'This is a DELETE request'})
    
    def patch(self, request):
        return Response({'message': 'This is a PATCH request'})