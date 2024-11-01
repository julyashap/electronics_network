from rest_framework import serializers
from suppliers.models import Supplier, Product


class ProductSupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('pk', 'name', 'model', 'realized_at',)
        read_only_fields = ['pk']


class SupplierSerializer(serializers.ModelSerializer):
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

    def create(self, validated_data):
        products = validated_data.pop('products')

        supplier = Supplier.objects.create(**validated_data)

        for product in products:
            Product.objects.create(**product, supplier=supplier)

        return supplier


class SupplierUpdateSerializer(serializers.ModelSerializer):
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


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('pk', 'name', 'model', 'realized_at', 'supplier',)
        read_only_fields = ['pk']
