
from django.urls import path

from product.views import *

urlpatterns = [
    path('product/', ProductListView.as_view()),
    path('product/detail/<int:pk>/', ProductDetailView.as_view()),
    path('product/create/', CreateProductView.as_view()),
    path('product/update/', UpdateProductView.as_view()),
    path('product/delete/', DeleteProductView.as_view()),

    path('prod/', ProductViewSet.as_view({'get': 'list',
                                          'post': 'create'})),
    path('prod/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve',
                                                   'put': 'update',
                                                   'patch': 'partial_update',
                                                   'delete': 'destroy'})),
    ]
