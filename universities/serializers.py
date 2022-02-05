from rest_framework import serializers
from .models import (
    Partner,
    Counter,
    PartnerType,
    Faculty
)
from countries.serializers import CountryListSerializer
#Detailed partner by pk

#showl all partners with filter type

class CounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counter
        fields = (
            'counter_value',
            'counter_text',
        )

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = (
            'text',
        )

class PartnerTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerType
        fields = (
            'title',
        )

class PartnerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = (
            'pk',
            'partner_image',
            'partner_name',
            'location',
            'payment',
        )

class PartnerDetailSerializer(serializers.ModelSerializer):
    country = CountryListSerializer()
    counters = CounterSerializer(many=True)
    faculties = FacultySerializer(many=True)
    partner_type = PartnerTypeSerializer()
    class Meta:
        model = Partner
        fields = (
            'pk',
            'partner_name',
            'partner_image',
            'foundation_year',
            'location',
            'payment',
            'country',
            'counters',
            'about_text',
            'about_video_url',
            'faculties',
            'partner_type',
        )