from rest_framework import serializers
from .models import (
    Country, 
    AboutImage,
)
from translations.models import (
    CountryTranslation,
    TranslationLanguage,
)

class TranslationLanguageSearializer(serializers.ModelSerializer):
    class Meta:
        model = TranslationLanguage
        fields = (
            'title',
        )



class AboutImagesSerializer(serializers.ModelSerializer):
    about_image_url = serializers.SerializerMethodField()
    class Meta:
        model = AboutImage
        fields = (
            'pk',
            'about_image_url',
        )

    def get_about_image_url(self, about_image):
        request = self.context.get('request')
        about_image_url = about_image.image.url
        return request.build_absolute_uri(about_image_url)

class CountryTranslationsSearializer(serializers.ModelSerializer):
    language = TranslationLanguageSearializer()
    class Meta:
        model = CountryTranslation
        fields = (
            'language',
            'country_name',
            'banner_title',
            'banner_sub_title',
            'about_text',
            'advantage_1',
            'advantage_2',
            'advantage_3',
            'advantage_4',
        )

class CountryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = (
            'pk',
            'country_name',
            'country_logo'
        )

class CountryDetailSerializer(serializers.ModelSerializer):
    about_images = AboutImagesSerializer(many=True)
    country_translations = CountryTranslationsSearializer(many=True)
    class Meta:
        model = Country
        fields = (
            'pk',
            'about_images',
            'banner_image',
            'country_translations',
        )