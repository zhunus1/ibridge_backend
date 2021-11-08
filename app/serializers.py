from rest_framework import serializers
from .models import (
    PartnerLogo,
    Counter,
    Country,
    University,
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

class CounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counter
        fields = (
            'pk',
            'name',
            'number',
        )

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = (
            'pk',
            'name',
        )

class CountrySerializer(serializers.ModelSerializer):
    universities = UniversitySerializer(many=True)
    class Meta:
        model = Country
        fields = (
            'pk',
            'name',
            'universities',
        )


class FormSerializer(serializers.Serializer):
    first_name = serializers.CharField(
        max_length=255,
    )
    last_name = serializers.CharField(
        max_length=255,
    )
    phone_number = serializers.CharField(
        max_length=128,
    )

class CalculatorFormSerializer(serializers.Serializer):
    first_name = serializers.CharField(
        max_length=255,
    )
    last_name = serializers.CharField(
        max_length=255,
    )
    phone_number = serializers.CharField(
        max_length=128,
    )
    comments = serializers.CharField()
