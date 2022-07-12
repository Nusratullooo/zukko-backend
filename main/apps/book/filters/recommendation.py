from django_filters.rest_framework import CharFilter

from ...common.filters.base_filter import BaseFilter
from ..models.recommendation import Recommendation


class RecommendationFilterSet(BaseFilter):
    title = CharFilter(field_name="book__title", lookup_expr="exact")
    author = CharFilter(field_name="book__author", lookup_expr="exact")

    class Meta:
        model = Recommendation
        fields = []
