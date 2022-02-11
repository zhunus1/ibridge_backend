from rest_framework import serializers
from .models import (
    PartnerLogo,
    Form,
    SeoText
)

class LogoSerializer(serializers.ModelSerializer):
    logo_url = serializers.SerializerMethodField()
    class Meta:
        model = PartnerLogo
        fields = (
            'pk',
            'name',
            'logo_url',
        )

    def get_logo_url(self, logo):
        request = self.context.get('request')
        logo_url = logo.image.url
        return request.build_absolute_uri(logo_url)

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = (
            'first_name',
            'last_name',
            'phone_number',
        )

class CalculatorFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = (
            'first_name',
            'last_name',
            'phone_number',
            'comments',
        )

class SeoTexterializer(serializers.ModelSerializer):
    class Meta:
        model = SeoText
        fields = (
            'text',
        )