from rest_framework import serializers
from suppliers.models import Supplier, Product
from suppliers.validators import SupplierLinkValidator, ProductSupplierValidator


class ProductSupplierSerializer(serializers.ModelSerializer):
    """Класс сериализатора объектов модели Product для использования в сериализаторах модели Supplier"""

    class Meta:
        model = Product
        fields = ('pk', 'name', 'model', 'realized_at',)
        read_only_fields = ['pk']


class SupplierSerializer(serializers.ModelSerializer):
    """Класс сериализатора объектов модели Supplier"""

    products = ProductSupplierSerializer(many=True, required=True)

    class Meta:
        model = Supplier
        fields = (
            'pk',
            'name',
            'email',
            'country',
            'city',
            'street',
            'house_number',
            'debt_to_supplier',
            'supplier_link',
            'level',
            'created_at',
            'products',
        )
        read_only_fields = ['pk', 'level', 'created_at']
        validators = [SupplierLinkValidator()]

    def create(self, validated_data):
        products = validated_data.pop('products')

        supplier = Supplier.objects.create(**validated_data)

        for product in products:
            Product.objects.create(**product, supplier=supplier)

        return supplier


class SupplierUpdateSerializer(serializers.ModelSerializer):
    """Класс сериализатора объектов модели Supplier при их обновлении"""

    class Meta:
        model = Supplier
        fields = (
            'pk',
            'name',
            'email',
            'country',
            'city',
            'street',
            'house_number',
            'debt_to_supplier',
            'supplier_link',
            'level',
            'created_at',
        )
        read_only_fields = ['pk', 'level', 'created_at', 'debt_to_supplier']
        validators = [SupplierLinkValidator()]


class ProductCreateSerializer(serializers.ModelSerializer):
    """Класс сериализатора для создания объектов модели Product"""

    class Meta:
        model = Product
        fields = ('pk', 'name', 'model', 'realized_at', 'supplier',)
        read_only_fields = ['pk']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.get('context').get('request')
        self.fields['supplier'].validators.append(ProductSupplierValidator(self.request.user))
        super().__init__(*args, **kwargs)


class ProductSerializer(serializers.ModelSerializer):
    """Класс сериализатора объектов модели Product"""

    class Meta:
        model = Product
        fields = ('pk', 'name', 'model', 'realized_at', 'supplier',)
        read_only_fields = ['pk']
