from django.urls import path
from . import views

app_ame = 'api'

urlpatterns = [
    path('item/', views.ItemView.as_view(), name='item'),
]