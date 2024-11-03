from rest_framework import permissions


class IsOwnerSupplier(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.user


class IsOwnerProduct(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.supplier.user
