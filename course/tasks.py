from datetime import datetime

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from timezone_field.backends import pytz

from users.models import User


@shared_task
def send_update_course(emails: list) -> None:

    send_mail(subject="Курс обновлен!", message="Course update", from_email=settings.EMAIL_HOST_USER, recipient_list=emails)



"""
проверка пользователей по дате входа
"""


@shared_task()
def block_user(*args, **kwargs):
    tz = pytz.timezone('Europe/Moscow')
    users = User.objects.all()
    for user in users:
        if user.last_login:
            diff = datetime.now(tz) - user.last_login

            if diff and diff.days >= 30:
                user.is_active = False
                user.save()