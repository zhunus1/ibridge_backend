from rest_framework import serializers
from .models import (
    Partner,
    Counter,
    PartnerType,
    Faculty,
    Program,
)

from translations.models import PartnerTranslation
from countries.serializers import (
    TranslationLanguageSearializer,
    CountrySlugSerializer
)

#Detailed partner by pk

#showl all partners with filter type

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = (
            'title',
        )

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
    country = CountrySlugSerializer()
    class Meta:
        model = Partner
        lookup_field  = 'partner_slug'
        fields = (
            'pk',
            'partner_slug',
            'partner_name',
            'partner_image',
            'country',
            'partner_translations',
        )

class PartnerTranslationDetailSerializer(serializers.ModelSerializer):
    language = TranslationLanguageSearializer()
    faculties = FacultySerializer(many=True)
    partner_type = PartnerTypeSerializer()
    counters = CounterSerializer(many=True)
    programs = ProgramSerializer(many=True)
    class Meta:
        model = PartnerTranslation
        fields = (
            'language',
            'partner_name',
            'foundation_year',
            'location',
            'payment',
            'programs',
            'counters',
            'about_text',
            'faculties',
            'partner_type',
        )
        

class PartnerDetailSerializer(serializers.ModelSerializer):
    partner_translations = PartnerTranslationDetailSerializer(many=True)
    country = CountrySlugSerializer()
    class Meta:
        model = Partner
        lookup_field = 'partner_slug'
        fields = (
            'pk',
            'partner_slug',
            'country',
            'partner_image',
            'about_video_url',
            'partner_translations',
        )
    
class PartnerFilterSerializer(serializers.Serializer):
    country = serializers.CharField(required=False)
    partner_type = serializers.CharField(required=False)
