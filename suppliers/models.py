from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Supplier(models.Model):
    LEVEL_CHOICES = [
        (0, 'Завод'),
        (1, 'Розничная сеть / Индивидуальный предприниматель'),
        (2, 'Индивидуальный предприниматель'),
    ]

    name = models.CharField(max_length=100, verbose_name='название')
    debt_to_supplier = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='задолженность')
    created_at = models.DateTimeField(verbose_name='дата создания')
    level = models.IntegerField(choices=LEVEL_CHOICES, default=0, verbose_name='уровень в иерархии')

    supplier_link = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='поставщик', **NULLABLE)

    def __str__(self):
        return f"supplier {self.name}"

    class Meta:
        verbose_name = 'поставщик'
        verbose_name_plural = 'поставщики'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    model = models.CharField(max_length=250, verbose_name='модель')
    realized_at = models.DateTimeField(verbose_name='дата выхода')

    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='поставщик', related_name='products')

    def __str__(self):
        return f"product {self.name} {self.model}"

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Contact(models.Model):
    email = models.EmailField(unique=True, verbose_name='email')
    country = models.CharField(max_length=100, verbose_name='страна')
    city = models.CharField(max_length=100, verbose_name='город')
    street = models.CharField(max_length=250, verbose_name='улица')
    house_number = models.PositiveIntegerField(verbose_name='номер дома')

    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='поставщик', related_name='contacts')

    def __str__(self):
        return f"contact {self.email}"

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'
