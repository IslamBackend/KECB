from django.db import models

from apps.home.constants import PAGE_CHOICES


class Banner(models.Model):
    title = models.CharField(max_length=125, verbose_name='Заголовок')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='banner_image', verbose_name='Изображение')
    page = models.CharField(max_length=30, choices=PAGE_CHOICES, unique=True, verbose_name='Страница')

    def __str__(self):
        return f'Баннер для {self.title}'

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'
        db_table = 'banner'


class SocialInfo(models.Model):
    image = models.ImageField(upload_to='site_image', verbose_name='Логотип')
    phone_number_first = models.CharField(max_length=20, null=True, blank=True, verbose_name='Первый номер телефона')
    phone_number_second = models.CharField(max_length=20, null=True, blank=True, verbose_name='Второй номер телефона')
    email = models.EmailField(null=True, blank=True, verbose_name='Электронная почта')
    working_hours = models.CharField(max_length=100, null=True, blank=True, verbose_name='Часы работы')
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True, verbose_name="Долгота")
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True, verbose_name="Широта")
    telegram_url = models.URLField(null=True, blank=True, verbose_name='Telegram')
    whatsapp_url_first = models.URLField(null=True, blank=True, verbose_name='Первый WhatsApp')
    whatsapp_url_second = models.URLField(null=True, blank=True, verbose_name='Второй WhatsApp')
    instagram_url = models.URLField(null=True, blank=True, verbose_name='Instagram')
    youtube_url = models.URLField(null=True, blank=True, verbose_name='YouTube')
    facebook_url = models.URLField(null=True, blank=True, verbose_name='Facebook')
    twitter_url = models.URLField(null=True, blank=True, verbose_name='Twitter')

    def __str__(self):
        return f'Информация о сайте'

    class Meta:
        verbose_name = 'Информация о сайте'
        verbose_name_plural = 'Информации о сайте'
        db_table = 'social_info'


class KoreanSite(models.Model):
    logo = models.ImageField(upload_to='korean_site_logos', verbose_name="Логотип")
    name = models.CharField(max_length=255, verbose_name="Название")
    url = models.URLField(verbose_name="Ссылка")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Корейский сайт"
        verbose_name_plural = "Корейские сайты"
        db_table = 'korean_sites'
