import types

from django.db import connection
from django.db.models.manager import Manager
from django.db.models.query import QuerySet, RawQuerySet
import public

class CountMixin:
    queryset_count = None

    def setcount(self,count):
        self.queryset_count = count
        return self

def count(self):
    return self.queryset_count

@public.add
class ListViewQuerySet(CountMixin,QuerySet):
    @classmethod
    def as_manager(cls):
        def get_queryset(self):
            return ListViewQuerySet(self.model, using=self._db)

        manager = super(ListViewQuerySet, cls).as_manager()
        manager.get_queryset = types.MethodType(get_queryset, manager)
        manager.count = types.MethodType(count, manager)
        return manager

@public.add
class ListViewRawQuerySet(CountMixin,RawQuerySet):
    def count(self):
        return self.queryset_count

    @classmethod
    def as_manager(cls):
        def raw(self, raw_query, params=None, *args, **kwargs):
            return ListViewRawQuerySet(
                raw_query=raw_query,
                model=self.model,
                params=params,
                using=self._db,
                *args, **kwargs
            )

        manager = Manager.from_queryset(cls)()
        manager._built_with_as_manager = True
        manager.raw = types.MethodType(raw, manager)
        manager.count = types.MethodType(count, manager)
        return manager
    as_manager.queryset_only = True
