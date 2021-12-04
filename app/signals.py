from django.db.models import signals
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
import requests
from django.core.mail import EmailMessage
from .models import (
    Form,
)
from django_q.tasks import async_task

bot_token = settings.TELEGRAM_BOT_API

def send_telegram(message):
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=-1001150175962' + '&parse_mode=Markdown&text=' + message
    response = requests.get(send_text)
    return response.status_code

def send_yandex(message):
    email = EmailMessage('Форма обратной связи', message, to=['admissions@ibridge.kz'])
    email.send()


def send_bitrix(params):
    if 'FIELDS[COMMENTS]' in params:
        url = 'https://ibridge.bitrix24.kz/rest/1/hvtvs3w97wbm6jm2/crm.lead.add.json'
    else:
        url = 'https://ibridge.bitrix24.kz/rest/1/40df1gu85r4s1itm/crm.lead.add.json'
    response = requests.post(url, params=params)
    return response.status_code


@receiver(post_save, sender=Form)
def save_form(sender, instance, created, **kwargs):
    if created:
        if instance.comments:
            message = "Имя: %s \nФамилия: %s \nНомер телефона: %s \nКалькулятор: %s" % (instance.first_name, instance.last_name, instance.phone_number, instance.comments)
            params = {
                'FIELDS[TITLE]': 'Калькулятор обучения',
                'FIELDS[NAME]':instance.first_name,
                'FIELDS[LAST_NAME]':instance.last_name,
                'FIELDS[PHONE][0][VALUE]':instance.phone_number,
                'FIELDS[COMMENTS]':instance.comments,
            }
        else:
            message = "Имя: %s \nФамилия: %s \nНомер телефона: %s" % (instance.first_name, instance.last_name, instance.phone_number)
            params = {
                'FIELDS[TITLE]': 'Форма обратной связи',
                'FIELDS[NAME]':instance.first_name,
                'FIELDS[LAST_NAME]':instance.last_name,
                'FIELDS[PHONE][0][VALUE]':instance.phone_number,
            }
        async_task('app.signals.send_telegram', message)
        async_task('app.signals.send_yandex', message)
        async_task('app.signals.send_bitrix', params)
