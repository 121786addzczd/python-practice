from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ItemsSerializer
from rest_framework import status

class ItemView(APIView):

    serializer_class = ItemsSerializer

    def get(self, request):
        return Response({'message': 'This is a GET request'})
    
    def post(self, request):
        print(f"Request Data={request.data}")
        serializer = self.serializer_class(data=request.data)
        print(serializer)

        # バリデーション
        # print(serializer.is_valid(raise_exception=True))
        # print(serializer.errors)

        if serializer.is_valid(raise_exception=True):
            serializer.save() # 保存(crate)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data)
    
    def put(self, request):
        return Response({'message': 'This is a PUT request'})
    
    def delete(self, request):
        return Response({'message': 'This is a DELETE request'})
    
    def patch(self, request):
        return Response({'message': 'This is a PATCH request'})