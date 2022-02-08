from rest_framework import viewsets
from django.shortcuts import render
from .models import Partner
from .serializers import (
    PartnerDetailSerializer,
    PartnerListSerializer, 
    PartnerFilterSerializer
)

# Create your views here.


class PartnerViewSet(viewsets.ReadOnlyModelViewSet):
    
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

    def filter_queryset(self, queryset):
        if self.action == 'list':
            serializer = PartnerFilterSerializer(data=self.request.query_params)
            serializer.is_valid(raise_exception=True)
            queryset = queryset.filter(
                partner_translations__partner_type__title=serializer.validated_data['partner_type'],
                country__country_name=serializer.validated_data['country']
            )
        return super().filter_queryset(queryset)