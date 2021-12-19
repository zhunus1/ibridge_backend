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

def send_yandex(message):
    email = EmailMessage('Форма обратной связи', message, to=['admissions@ibridge.kz'])
    email.send()


def send_bitrix(params):
    url = 'https://ibridge.bitrix24.kz/rest/1/4b3cdysditcku813/crm.deal.add.json'
    response = requests.post(url, params=params)


@receiver(post_save, sender=Form)
def save_form(sender, instance, created, **kwargs):
    if created:
        if instance.comments:
            message = "Имя: %s \nФамилия: %s \nНомер телефона: %s \nКалькулятор: %s" % (instance.first_name, instance.last_name, instance.phone_number, instance.comments)
            name = "%s %s" % (instance.first_name, instance.last_name)
            comments = "%s \n %s" % (instance.phone_number, instance.comments)
            params = {
                'FIELDS[TITLE]': name,
                'FIELDS[COMMENTS]': comments,
                'FIELDS[SOURCE_ID]': 'WEB',
            }
        else:
            message = "Имя: %s \nФамилия: %s \nНомер телефона: %s" % (instance.first_name, instance.last_name, instance.phone_number)
            name = "%s %s" % (instance.first_name, instance.last_name)
            comments = "%s \n %s" % (instance.phone_number, instance.comments)
            params = {
                'FIELDS[TITLE]': name,
                'FIELDS[COMMENTS]': comments,
                'FIELDS[SOURCE_ID]': 'WEB',
            }

        async_task('app.signals.send_bitrix', params)
        async_task('app.signals.send_telegram', message)
        async_task('app.signals.send_yandex', message)
