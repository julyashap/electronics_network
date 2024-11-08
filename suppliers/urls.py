from django.urls import path
from suppliers.apps import SuppliersConfig
from suppliers.views import SupplierListAPIView, SupplierDestroyAPIView, SupplierRetrieveAPIView, \
    SupplierCreateAPIView, SupplierUpdateAPIView, ProductCreateAPIView, ProductUpdateAPIView, ProductDestroyAPIView

app_name = SuppliersConfig.name

urlpatterns = [
    path('', SupplierListAPIView.as_view(), name='supplier_list'),
    path('<int:pk>/', SupplierRetrieveAPIView.as_view(), name='supplier_retrieve'),
    path('create/', SupplierCreateAPIView.as_view(), name='supplier_create'),
    path('update/<int:pk>/', SupplierUpdateAPIView.as_view(), name='supplier_update'),
    path('destroy/<int:pk>/', SupplierDestroyAPIView.as_view(), name='supplier_destroy'),

    path('product/create/', ProductCreateAPIView.as_view(), name='product_create'),
    path('product/update/<int:pk>/', ProductUpdateAPIView.as_view(), name='product_update'),
    path('product/destroy/<int:pk>/', ProductDestroyAPIView.as_view(), name='product_destroy'),
]
