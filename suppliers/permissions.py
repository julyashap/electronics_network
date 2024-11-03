from rest_framework import permissions


class IsOwnerSupplier(permissions.BasePermission):
    """Класс проверки прав доступа для создателя текущего объекта поставщика"""

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user


class IsOwnerProduct(permissions.BasePermission):
    """Класс проверки прав доступа на продукты текущего поставщика"""

    def has_object_permission(self, request, view, obj):
        return request.user == obj.supplier.user
