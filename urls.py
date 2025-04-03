from django.urls import path
from .views import ProductListView, ProductDetailView, UserActivityView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('user-activity/', UserActivityView.as_view(), name='user-activity'),
]
