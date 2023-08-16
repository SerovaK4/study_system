from django.utils import timezone

from django.db import models

from config import settings
from users.models import User

NULLABLE = {
    'blank': True,
    'null': True
}


class Course(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    img = models.ImageField(upload_to='course/', verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    img = models.ImageField(upload_to='course/', verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)
    link_video = models.CharField(max_length=150, verbose_name='ссылка на видео', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, verbose_name='курс', related_name='lessons', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class Payment(models.Model):
    TITLE_PAYMENT_METHOD = [
        (1, 'Наличные'),
        (2, 'Перевод на счет',),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="пользователь")
    date_payment = models.DateTimeField(verbose_name="дата оплаты", default=timezone.now)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="оплаченный курс", related_name='payment',
                               **NULLABLE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name="оплаченный урок", related_name='payment',
                               **NULLABLE)
    payment = models.FloatField(verbose_name="сумма оплаты")
    payment_method = models.PositiveSmallIntegerField(choices=TITLE_PAYMENT_METHOD, default=1,
                                                      verbose_name='способ оплаты')

    def __str__(self):
        return f"{self.user}: {self.payment}"

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'


class Subscription(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="курс для подписки",
                               related_name="subscribe", **NULLABLE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="пользователь", related_name="subscribe", **NULLABLE)
    is_subscribe = models.BooleanField(default=False, verbose_name="подписка")

    def __str__(self):
        return f'{self.user}: {self.course}'


    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'
