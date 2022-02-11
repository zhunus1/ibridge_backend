import requests
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .permissions import APIKeyPermission
from django.utils.translation import *
from django.conf import settings

from .models import (
    PartnerLogo,
    Form,
)
from .serializers import (
    LogoSerializer,
    FormSerializer,
    CalculatorFormSerializer,
)


# Create your views here
class LogoListView(APIView):

    def get(self, request, format=None):
        logos = PartnerLogo.objects.all()
        serializer = LogoSerializer(logos, context={"request": request}, many=True)
        return Response(serializer.data)

class FormView(APIView):
    permission_classes = (APIKeyPermission,)

    def post(self, request):
        serializer = FormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CalculatorFormView(APIView):
    permission_classes = (APIKeyPermission,)

    def post(self, request):
        serializer = CalculatorFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
