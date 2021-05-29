from django_filters import rest_framework as filters
from mainapp.models import Post


class PostFilter(filters.FilterSet):

    created = filters.DateTimeFromToRangeFilter()

    class Meta:
        model = Post
        fields = ['created',]