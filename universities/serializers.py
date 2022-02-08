# from rest_framework import serializers
# from .models import (
#     Partner,
#     Counter,
#     PartnerType,
#     Faculty
# )
# #from translations.models import PartnerTranslation
# from countries.serializers import TranslationLanguageSearializer

# #Detailed partner by pk

# #showl all partners with filter type

# class CounterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Counter
#         fields = (
#             'counter_value',
#             'counter_text',
#         )

# class FacultySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Faculty
#         fields = (
#             'text',
#         )

# class PartnerTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PartnerType
#         fields = (
#             'title',
#         )

# class PartnerListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Partner
#         fields = (
#             'pk',
#             'partner_name',
#             'partner_image',
#             'about_video_url',
#         )

# class PartnerTranslationSerializer(serializers.ModelSerializer):
#     language = TranslationLanguageSearializer()
#     faculties = FacultySerializer(many=True)
#     partner_type = PartnerTypeSerializer()
#     counters = CounterSerializer(many=True)
#     class Meta:
#         model = PartnerTranslation
#         fields = (
#             'language',
#             'partner_name',
#             'foundation_year',
#             'location',
#             'payment',
#             'about_text',
#             'faculties',
#             'partner_type',
#             'counters',
#         )

# class PartnerDetailSerializer(serializers.ModelSerializer):
#     partner_translations = PartnerTranslationSerializer(many=True)
#     class Meta:
#         model = Partner
#         fields = (
#             'pk',
#             'partner_name',
#             'partner_image',
#             'about_video_url',
#             'partner_translations',
#         )
    
# class PartnerFilterSerializer(serializers.Serializer):
#     country = serializers.CharField(required=False)
#     partner_type = serializers.CharField(required=False)
