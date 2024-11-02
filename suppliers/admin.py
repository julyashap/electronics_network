from django.contrib import admin
from suppliers.models import Supplier, Product


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    """Класс добавления модели Supplier в административную панель"""

    list_display = ('pk', 'name', 'supplier_link', 'debt_to_supplier', 'level', 'email', 'city',)
    list_filter = ('city',)
    search_fields = ('city',)

    actions = ['reset_dept_to_supplier']

    def reset_dept_to_supplier(self, request, queryset):
        queryset.update(debt_to_supplier=0)
        self.message_user(request, 'Задолженность для выбранных объектов успешно сброшена!')

    reset_dept_to_supplier.short_description = 'Сбросить размер задолженности'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Класс добавления модели Product в административную панель"""

    list_display = ('pk', 'name', 'model', 'realized_at', 'supplier',)
    list_filter = ('name',)
