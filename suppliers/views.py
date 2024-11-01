from rest_framework import generics
from config import settings
from suppliers.models import Supplier, Product
from suppliers.paginators import SuppliersPagination
from suppliers.serializers import SupplierSerializer, SupplierUpdateSerializer, ProductSerializer
from rest_framework.filters import SearchFilter


class SupplierCreateAPIView(generics.CreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

    def perform_create(self, serializer):
        supplier = serializer.save(created_at=settings.NOW)
        if supplier.supplier_link:
            supplier.level = supplier.supplier_link.level + 1
        supplier.save()


class SupplierUpdateAPIView(generics.UpdateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierUpdateSerializer

    def perform_update(self, serializer):
        supplier = serializer.save()
        if supplier.supplier_link:
            supplier.level = supplier.supplier_link.level + 1
        supplier.save()


class SupplierRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class SupplierListAPIView(generics.ListAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

    filter_backends = (SearchFilter,)
    search_fields = ['country']

    pagination_class = SuppliersPagination


class SupplierDestroyAPIView(generics.DestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
