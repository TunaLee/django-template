# Python
import operator
from functools import reduce

# Django
from django.db import models

# DRF
from rest_framework.compat import distinct
from rest_framework.filters import SearchFilter


# Class Section
class ClubsSearchFilter(SearchFilter):
    search_or_param = 'and'
    search_and_param = 'or'
    search_exclude_param = 'exclude'

    def get_search_terms(self, request):
        params = request.query_params.get(self.search_param, '')
        params = params.replace('\x00', '')
        params = params.replace(',', ' ')
        return params.split()

    def filter_queryset(self, request, queryset, view):
        search_fields = self.get_search_fields(view, request)
        search_terms = self.get_search_terms(request)

        print('search_terms : ', search_terms)

        if not search_fields or not search_terms:
            return queryset

        orm_lookups = [
            self.construct_search(str(search_field))
            for search_field in search_fields
        ]

        base = queryset
        conditions = []
        for search_term in search_terms:
            queries = [
                models.Q(**{orm_lookup: search_term})
                for orm_lookup in orm_lookups
            ]
            conditions.append(reduce(operator.or_, queries))
        queryset = queryset.filter(reduce(operator.and_, conditions))

        print('queryset : ', queryset)

        if self.must_call_distinct(queryset, search_fields):
            queryset = distinct(queryset, base)
        return queryset
