from django.db import models


NULLABLE = {
    'blank': True,
    'null': True
}


class Course(models.Model):

    name = models.CharField(max_length=150, verbose_name='наименование')
    img = models.ImageField(upload_to='course/', verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:

        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    img = models.ImageField(upload_to='course/', verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание',**NULLABLE)
    link_video = models.CharField(max_length=150, verbose_name='ссылка на видео',**NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, verbose_name='курс', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'