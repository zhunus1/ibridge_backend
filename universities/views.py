from rest_framework import viewsets
from django.shortcuts import render
from .models import Partner
# from .serializers import (
#     PartnerDetailSerializer,
#     PartnerListSerializer, 
#     PartnerFilterSerializer
# )

# Create your views here.


class PartnerViewSet(viewsets.ReadOnlyModelViewSet):
    pass
    
    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return PartnerListSerializer
    #     return PartnerDetailSerializer
    
    # def get_queryset(self):
    #     queryset = Partner.objects.all()
    #     country = self.request.query_params.get('country', None)
    #     partner_type = self.request.query_params.get('type', None)
    #     if country is not None and partner_type is not None:
    #         queryset = queryset.filter(country__country_name=country, partner_translations__partner_type__title=partner_type)
    #     return queryset

    #filter by country and type