from django.urls import path
from . import views

app_ame = 'apiv2'

urlpatterns = [
    path('item/', views.ItemModelView.as_view(), name='item_model'),
    path('item/<int:pk>/', views.ItemModelDetailView.as_view(), name='item_model_detail'),
]