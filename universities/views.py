from rest_framework import viewsets
from django.shortcuts import render
from .models import Partner
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter
from .serializers import (
    PartnerDetailSerializer,
    PartnerListSerializer, 
    PartnerFilterSerializer
)
from .filters import PartnerFilter
# Create your views here.


class PartnerViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = (SearchFilter, filters.DjangoFilterBackend)
    search_fields = ('country__country_name', 'partner_name', 'partner_translations__faculties__text', 'partner_translations__programs__title', 'partner_type__title')
    filter_class = PartnerFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return PartnerListSerializer
        return PartnerDetailSerializer

    def get_queryset(self):
        queryset = Partner.objects.all()
        if self.action == 'list':
            queryset = Partner.objects \
                    .prefetch_related('partner_translations') \
                    .order_by('created') \
                    .all()
        return queryset
