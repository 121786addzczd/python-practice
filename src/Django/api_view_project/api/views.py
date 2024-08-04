from rest_framework.response import Response
from rest_framework.views import APIView

class ItemView(APIView):
    
    def get(self, request):
        return Response({'method': 'get'})
    
    def post(self, request):
        return Response({'method': 'psot'})
    
    def put(self, request):
        return Response({'method': 'put'})
    
    # def delete(self, request):
    #     return Response({'method': 'delete'})
    
    def patch(self, request):
        return Response({'method': 'patce'})