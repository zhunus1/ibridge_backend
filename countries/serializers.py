from rest_framework import serializers
from .models import (
    Country, 
    AboutImage,
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

class CountryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = (
            'pk',
            'country_name',
        )

class CountryDetailSerializer(serializers.ModelSerializer):
    about_image = AboutImagesSerializer(many=True)
    class Meta:
        model = Country
        fields = (
            'pk',
            'country_name',
            'banner_title',
            'banner_sub_title',
            'banner_image',
            'about_text',
            'about_image',
            'advantage_1',
            'advantage_2',
            'advantage_3',
            'advantage_4',
        )