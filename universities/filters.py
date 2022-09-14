import django_filters as filters
from .models import Partner
import django_filters

class PartnerFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='partner_translations__partner_type__title')
    country_name = django_filters.CharFilter(method='my_custom_filter')

    class Meta:
        model = Partner
        fields = (
            'title',
        )
    
    def my_custom_filter(self, queryset, name, value):
        return queryset.filter(
            Q(country__country_name__icontains=value) | Q(country__country_slug__icontains=value)
        )
