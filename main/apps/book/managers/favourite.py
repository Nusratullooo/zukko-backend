from django.db.models import Avg
from django.db.models.functions import Coalesce

from ...common.managers import BaseManager


class FavouriteManager(BaseManager):
    def create_favourite_instance(self, owner, data):
        return self.create(**data, owner=owner)

    def filter_favourites(self):
        return (
            self.select_related("book")
            .prefetch_related("book__rates")
            .annotate(rating=Coalesce(Avg("book__rates__point"), float(0)))
        )
