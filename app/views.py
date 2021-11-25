import requests
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .permissions import APIKeyPermission
from django.utils.translation import *
from django.core.mail import EmailMessage
from django.conf import settings

from .models import (
    PartnerLogo,
)
from .serializers import (
    LogoSerializer,
    FormSerializer,
    CalculatorFormSerializer,
)

bot_token = settings.TELEGRAM_BOT_API

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
        serializer.is_valid(raise_exception=True)

        params = {
            'FIELDS[TITLE]': 'Форма обратной связи',
            'FIELDS[NAME]':serializer.validated_data['first_name'],
            'FIELDS[LAST_NAME]':serializer.validated_data['last_name'],
            'FIELDS[PHONE][0][VALUE]':serializer.validated_data['phone_number'],
        }
        message = "Имя: %s \nФамилия: %s \nНомер телефона: %s" % (serializer.validated_data['first_name'], serializer.validated_data['last_name'], serializer.validated_data['phone_number'])
        # email = EmailMessage('Форма обратной связи', message, to=['admissions@ibridge.kz'])
        # email.send()

        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=-1001150175962' + '&parse_mode=Markdown&text=' + message
        response = requests.get(send_text)

        #response = requests.post('https://b24-ofa1r8.bitrix24.ru/rest/1/gz9zumkmsvsncx45/crm.lead.add.json', params=params)
        if response.status_code==200:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(data={'Error':response.status_code})

class CalculatorFormView(APIView):
    permission_classes = (APIKeyPermission,)

    def post(self, request):
        serializer = CalculatorFormSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        params = {
            'FIELDS[TITLE]': 'Калькулятор обучения',
            'FIELDS[NAME]':serializer.validated_data['first_name'],
            'FIELDS[LAST_NAME]':serializer.validated_data['last_name'],
            'FIELDS[PHONE][0][VALUE]':serializer.validated_data['phone_number'],
            'FIELDS[COMMENTS]':serializer.validated_data['comments'],
        }
        message = "Имя: %s \nФамилия: %s \nНомер телефона: %s \nКалькулятор: %s" % (serializer.validated_data['first_name'], serializer.validated_data['last_name'], serializer.validated_data['phone_number'], serializer.validated_data['comments'])
        email = EmailMessage('Калькулятор обучения', message, to=['admissions@ibridge.kz'])
        email.send()

        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=-1001150175962' + '&parse_mode=Markdown&text=' + message
        response = requests.get(send_text)

        response = requests.post('https://b24-ofa1r8.bitrix24.ru/rest/1/ykgl57kxbmegq1m5/crm.lead.add.json', params=params)
        if response.status_code==200:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(data={'Error':response.status_code})
