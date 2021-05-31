from rest_framework.pagination import PageNumberPagination


class LargeResultsSetPagination(PageNumberPagination):
    """Pagination class for large pages"""
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10000


class StandardResultsSetPagination(PageNumberPagination):
    """Pagination class for short pages"""
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10000
