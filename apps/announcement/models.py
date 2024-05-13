from django.db import models

from apps.announcement.constants import RUBRIC_CHOICES


class Rubric(models.Model):
    title = models.CharField(max_length=50, choices=RUBRIC_CHOICES, unique=True)

    def __str__(self):
        return self.get_title_display()

    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'
        db_table = 'rubric'


class Announcement(models.Model):
    rubric = models.ForeignKey(Rubric, related_name='announcement', on_delete=models.CASCADE, verbose_name='Рубрика')
    title = models.CharField(max_length=125, verbose_name='Заголовок')
    image = models.ImageField(upload_to='announcements', verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-created_at']
        db_table = 'announcement'


class AnnouncementFile(models.Model):
    title = models.CharField(max_length=125, verbose_name='Название файла')
    file_path = models.FileField(upload_to='announcement_files', max_length=255, verbose_name='Путь к файлу')
    announcement = models.ForeignKey(
        Announcement,
        on_delete=models.CASCADE,
        related_name='files',
        verbose_name='Объявление'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Файл объявления'
        verbose_name_plural = 'Файлы объявлений'
        db_table = 'announcement_file'


class AnnouncementVideo(models.Model):
    link = models.URLField(max_length=255, verbose_name='Ссылка на видео')
    announcement = models.ForeignKey(
        Announcement,
        related_name='videos',
        on_delete=models.CASCADE,
        verbose_name='Объявление'
    )

    def __str__(self):
        return self.link

    class Meta:
        verbose_name = 'Видео объявления'
        verbose_name_plural = 'Видео объявлений'
        db_table = 'announcement_video'


class AnnouncementImage(models.Model):
    image = models.ImageField(upload_to='announcement_images', verbose_name='Изображение')
    announcement = models.ForeignKey(
        Announcement,
        related_name='images',
        on_delete=models.CASCADE,
        verbose_name='Объявление'
    )

    def __str__(self):
        return str(self.image)

    class Meta:
        verbose_name = 'Изображение объявления'
        verbose_name_plural = 'Изображения объявлений'
        db_table = 'announcement_image'
