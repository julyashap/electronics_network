from django.db import models
from config import settings

NULLABLE = {'null': True, 'blank': True}


class Supplier(models.Model):
    """Класс модели поставщика в системе"""

    LEVEL_CHOICES = [
        (0, 'Завод'),
        (1, 'Розничная сеть / Индивидуальный предприниматель'),
        (2, 'Индивидуальный предприниматель'),
    ]

    name = models.CharField(max_length=100, verbose_name='название')

    email = models.EmailField(unique=True, verbose_name='email', **NULLABLE)
    country = models.CharField(max_length=100, verbose_name='страна', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='город', **NULLABLE)
    street = models.CharField(max_length=250, verbose_name='улица', **NULLABLE)
    house_number = models.PositiveIntegerField(verbose_name='номер дома', **NULLABLE)

    debt_to_supplier = models.DecimalField(max_digits=12, decimal_places=2, default=0.00, verbose_name='задолженность')
    created_at = models.DateTimeField(verbose_name='дата создания')
    level = models.IntegerField(choices=LEVEL_CHOICES, default=0, verbose_name='уровень в иерархии')

    supplier_link = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='поставщик', **NULLABLE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='владелец', **NULLABLE)

    def __str__(self):
        return f"supplier {self.name}"

    class Meta:
        verbose_name = 'поставщик'
        verbose_name_plural = 'поставщики'


class Product(models.Model):
    """Класс модели продуктов поставщика в системе"""

    name = models.CharField(max_length=100, verbose_name='название')
    model = models.CharField(max_length=250, verbose_name='модель')
    realized_at = models.DateTimeField(verbose_name='дата выхода')

    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='поставщик', related_name='products')

    def __str__(self):
        return f"product {self.name} {self.model}"

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
