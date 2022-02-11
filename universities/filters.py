import django_filters as filters
from .models import Partner

class PartnerFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='partner_translations__partner_type__title')
    country_name = filters.CharFilter(field_name='country__country_name')

    class Meta:
        model = Partner
        fields = (
            'title',
            'country_name'
        )