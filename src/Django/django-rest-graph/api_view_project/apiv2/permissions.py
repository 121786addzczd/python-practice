from rest_framework.permissions import BasePermission
from . import views

class CustomPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        if isinstance(view, views.ItemModelDetailView):
            if request.method == 'DELETE':
                return False
        if request.META['REMOTE_ADDR'] == '127.0.0.1': # IP制御
            print(f"IPアドレス:{request.META['REMOTE_ADDR']}")
            return False
        if request.method == 'GET':
            return True
        print(view)
        return True