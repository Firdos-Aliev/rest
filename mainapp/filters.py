from django_filters import rest_framework as filters
from mainapp.models import Post


class PostFilter(filters.FilterSet):
    """
    Filter for post(created time)
    """

    created = filters.DateTimeFromToRangeFilter()

    class Meta:
        model = Post
        fields = ['created', ]
