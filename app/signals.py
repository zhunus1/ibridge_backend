from django.db.models import signals
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
import requests
import json
from django.core.mail import EmailMessage
from .models import (
    Form,
)
from django_q.tasks import async_task

bot_token = settings.TELEGRAM_BOT_API

def send_telegram(message):
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=-1001150175962' + '&parse_mode=Markdown&text=' + message
    response = requests.get(send_text)

def send_yandex(message):
    email = EmailMessage('Форма обратной связи', message, to=['admissions@ibridge.kz'])
    email.send()


def send_bitrix(params, contact):
    url = 'https://ibridge.bitrix24.kz/rest/1/fluv6268xjs8yywo/crm.contact.add.json'
    response = requests.post(url, params=contact)
    
    params['FIELDS[CONTACT_ID]'] = response.json()['result']

    url = 'https://ibridge.bitrix24.kz/rest/1/hf632uh1e28esic5/crm.deal.add.json'
    response = requests.post(url, params=params)

@receiver(post_save, sender=Form)
def save_form(sender, instance, created, **kwargs):
    if created:
        contact = {
            "FIELDS[NAME]": instance.first_name,
            "FIELDS[LAST_NAME]": instance.last_name,
            "FIELDS[TYPE_ID]": "CLIENT",
            "FIELDS[OPENED]": "Y",
            "FIELDS[SOURCE_ID]": "WEB",
            "FIELDS[PHONE][0][VALUE_TYPE]" :"WORK",
            "FIELDS[PHONE][0][VALUE]" :instance.phone_number,
        }

        if instance.comments:
            comments = instance.comments
            message = "Имя: %s \nФамилия: %s \nНомер телефона: %s \Комментарий: %s" % (instance.first_name, instance.last_name, instance.phone_number, instance.comments)
            params = {
                'FIELDS[TITLE]': 'Веб-сайт ibridge.kz',
                'FIELDS[COMMENTS]': comments,
                'FIELDS[SOURCE_ID]': 'WEB',
            }
        else:
            message = "Имя: %s \nФамилия: %s \nНомер телефона: %s" % (instance.first_name, instance.last_name, instance.phone_number)
            params = {
                'FIELDS[TITLE]': 'Веб-сайт ibridge.kz',
                'FIELDS[SOURCE_ID]': 'WEB',
            }
        
        async_task('app.signals.send_bitrix', params=params, contact=contact)
        async_task('app.signals.send_telegram', message)
        async_task('app.signals.send_yandex', message)
