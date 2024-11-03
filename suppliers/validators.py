from rest_framework.exceptions import ValidationError


class SupplierLinkValidator:
    def __call__(self, value):
        supplier = dict(value).get('supplier_link')

        if supplier and supplier.level == 2:
            raise ValidationError({'supplier_link': 'Вы не можете заказывать товары у этого поставщика!'})


class ProductSupplierValidator:
    def __init__(self, user):
        self.user = user

    def __call__(self, supplier):
        if supplier.user != self.user:
            raise ValidationError('Вы не можете создавать продукты другого поставщика!')
