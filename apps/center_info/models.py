from django.db import models

from apps.center_info.constants import ACTIVITY_CHOICES


class DirectorSpeech(models.Model):
    text = models.TextField(verbose_name='Текст')
    image = models.ImageField(upload_to='director_welcome/', verbose_name='Изображение')

    def __str__(self):
        return 'Приветственное слово директора'

    class Meta:
        verbose_name = 'Приветственное слово директора'
        verbose_name_plural = 'Приветственные слова директора'
        db_table = 'director_speech'


class CenterHistory(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='center_history/', verbose_name='Изображение')
    date = models.DateField(verbose_name='Дата')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'История и основная информация центра'
        verbose_name_plural = 'Истории и основная информация центра'
        ordering = ['-date']
        db_table = 'center_history'


class CenterActivity(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    activity_type = models.CharField(
        max_length=50,
        choices=ACTIVITY_CHOICES,
        unique=True,
        verbose_name='Тип деятельности'
    )
    description = models.TextField(verbose_name='Описание')
    video = models.URLField(verbose_name='Видео')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Деятельность центра'
        verbose_name_plural = 'Деятельности центра'
        db_table = 'center_activity'


class CenterActivityImage(models.Model):
    image = models.ImageField(upload_to='center_activity/', verbose_name='Изображение')
    center_activity = models.ForeignKey(
        CenterActivity,
        on_delete=models.CASCADE,
        null=True, blank=True,
        verbose_name='Деятельность центра',
        related_name='center_activity_images'
    )

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        db_table = 'center_activity_image'

