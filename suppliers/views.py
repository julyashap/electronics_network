from rest_framework import generics
from config import settings
from suppliers.models import Supplier, Product
from suppliers.paginators import SuppliersPagination
from suppliers.permissions import IsOwnerSupplier, IsOwnerProduct
from suppliers.serializers import SupplierSerializer, SupplierUpdateSerializer, ProductSerializer, \
    ProductCreateSerializer
from rest_framework.filters import SearchFilter


class SupplierCreateAPIView(generics.CreateAPIView):
    """Представление для создания объекта модели Supplier"""

    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

    def perform_create(self, serializer):
        supplier = serializer.save(created_at=settings.NOW, user=self.request.user)
        if supplier.supplier_link:
            supplier.level = supplier.supplier_link.level + 1
        supplier.save()


class SupplierUpdateAPIView(generics.UpdateAPIView):
    """Представление для обновления объекта модели Supplier"""

    queryset = Supplier.objects.all()
    serializer_class = SupplierUpdateSerializer
    permission_classes = [IsOwnerSupplier]

    def perform_update(self, serializer):
        supplier = serializer.save()
        if supplier.supplier_link:
            supplier.level = supplier.supplier_link.level + 1
        supplier.save()


class SupplierRetrieveAPIView(generics.RetrieveAPIView):
    """Представление для просмотра объекта модели Supplier"""

    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsOwnerSupplier]


class SupplierListAPIView(generics.ListAPIView):
    """Представление для просмотра списка объектов модели Supplier"""

    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

    filter_backends = (SearchFilter,)
    search_fields = ['country']

    pagination_class = SuppliersPagination


class SupplierDestroyAPIView(generics.DestroyAPIView):
    """Представление для удаления объекта модели Supplier"""

    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsOwnerSupplier]


class ProductCreateAPIView(generics.CreateAPIView):
    """Представление для создания объекта модели Product"""

    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer


class ProductUpdateAPIView(generics.UpdateAPIView):
    """Представление для обновления объекта модели Product"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsOwnerProduct]


class ProductDestroyAPIView(generics.DestroyAPIView):
    """Представление для удаления объекта модели Product"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsOwnerProduct]
