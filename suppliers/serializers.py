from rest_framework import serializers
from suppliers.models import Supplier, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('pk', 'name', 'model', 'relized_at',)
        read_only_fields = ['pk']


class SupplierSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, required=True)

    class Meta:
        model = Supplier
        fields = (
            'name',
            'email',
            'country',
            'city',
            'street',
            'house_number',
            'debt_to_supplier',
            'supplier_link',
            'products',
        )

    def create(self, validated_data):
        products = validated_data.pop('products')

        supplier = Supplier.objects.create(**validated_data)

        for product in products:
            Product.objects.create(**product, supplier=supplier)

        return supplier


class SupplierReadSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, source='products.all')

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
            'created_at',
            'level',
            'products',
        )


class ProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('pk', 'name', 'model', 'relized_at',)


class SupplierUpdateSerializer(serializers.ModelSerializer):
    products = ProductUpdateSerializer(many=True)

    class Meta:
        model = Supplier
        fields = (
            'name',
            'email',
            'country',
            'city',
            'street',
            'house_number',
            'supplier_link',
            'products',
        )

    def update(self, instance, validated_data):
        passed_products = validated_data.pop('products')

        instance.update(**validated_data)

        if passed_products:
            existing_products = {product.pk: product for product in instance.products.all()}

            for product in passed_products:
                product_pk = product.get('pk')

                if product_pk in existing_products:
                    existing_products[product_pk].update(**product)
                else:
                    Product.objects.create(**product, supplier=instance)

            passed_products_pks = [product.get('pk') for product in passed_products]

            for product_pk in existing_products.keys():
                if product_pk not in passed_products_pks:
                    existing_products[product_pk].delete()

        return instance
