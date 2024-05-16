from django.db import models

from apps.announcement.models import Rubric


class Gallery(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    rubric = models.ForeignKey(
        Rubric,
        related_name='gallery',
        on_delete=models.CASCADE,
        verbose_name='Рубрика')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фотогалерея'
        verbose_name_plural = 'Фотогалереи'
        ordering = ('-id',)
        db_table = 'gallery'


class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery_images', verbose_name='Изображение')
    gallery = models.ForeignKey(
        Gallery,
        on_delete=models.CASCADE,
        related_name='gallery_images',
        verbose_name='Галерея')

    class Meta:
        verbose_name = 'Изображение галереи'
        verbose_name_plural = 'Изображения галереи'
        db_table = 'gallery_images'


class EducationalMaterial(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    link = models.FileField(upload_to='educational_materials', verbose_name='Файл или ссылка')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Учебное пособие'
        verbose_name_plural = 'Учебные пособия'
        ordering = ('-id',)
        db_table = 'educational_material'
