from rest_framework import pagination


class SuppliersPagination(pagination.PageNumberPagination):
    """Класс пагинации для списка объектов модели Supplier"""

    page_size = 5
    page_query_param = 'page_size'
    max_page_size = 20
