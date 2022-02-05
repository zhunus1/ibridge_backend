from rest_framework import viewsets
from django.shortcuts import render
from .models import Partner
from .serializers import (
    PartnerDetailSerializer,
    PartnerListSerializer
)

# Create your views here.


class PartnerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Partner.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'list':
            return PartnerListSerializer
        return PartnerDetailSerializer
    

    #filter by country and type