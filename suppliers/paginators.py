from rest_framework import pagination


class SuppliersPagination(pagination.PageNumberPagination):
    page_size = 5
    page_query_param = 'page_size'
    max_page_size = 20
