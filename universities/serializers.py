from rest_framework import serializers
from .models import (
    Partner,
    Counter,
    PartnerType,
    Faculty
)

from translations.models import PartnerTranslation
from countries.serializers import TranslationLanguageSearializer

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
    language = TranslationLanguageSearializer()
    class Meta:
        model = PartnerType
        fields = (
            'title',
            'language',
        )


class PartnerTranslationListSerializer(serializers.ModelSerializer):
    language = TranslationLanguageSearializer()
    class Meta:
        model = PartnerTranslation
        fields = (
            'language',
            'partner_name',
            'location',
            'payment',
        )

class PartnerListSerializer(serializers.ModelSerializer):
    partner_translations = PartnerTranslationListSerializer(many=True)
    class Meta:
        model = Partner
        fields = (
            'pk',
            'partner_name',
            'partner_image',
            'partner_translations',
        )

class PartnerTranslationDetailSerializer(serializers.ModelSerializer):
    language = TranslationLanguageSearializer()
    faculties = FacultySerializer(many=True)
    partner_type = PartnerTypeSerializer()
    counters = CounterSerializer(many=True)
    class Meta:
        model = PartnerTranslation
        fields = (
            'language',
            'partner_name',
            'foundation_year',
            'location',
            'payment',
            'counters',
            'about_text',
            'faculties',
            'partner_type',
        )

class PartnerDetailSerializer(serializers.ModelSerializer):
    partner_translations = PartnerTranslationDetailSerializer(many=True)
    class Meta:
        model = Partner
        fields = (
            'pk',
            'partner_image',
            'about_video_url',
            'partner_translations',
        )
    
class PartnerFilterSerializer(serializers.Serializer):
    country = serializers.CharField(required=False)
    partner_type = serializers.CharField(required=False)
