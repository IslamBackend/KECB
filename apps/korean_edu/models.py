from django.db import models

from apps.korean_edu.constants import UNIVERSITY_TYPE_CHOICES


class UniversityInfo(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    image = models.ImageField(upload_to='university_image', verbose_name='Изображение')
    type = models.CharField(max_length=20, choices=UNIVERSITY_TYPE_CHOICES, verbose_name='Тип вуза')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    founding_year = models.PositiveIntegerField(verbose_name='Год основания')
    website = models.URLField(verbose_name='Ссылка на сайт')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Информация о вузе'
        verbose_name_plural = 'Информация о вузах'
        db_table = 'university_info'


class RecruitmentAnnouncement(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    video = models.URLField(null=True, blank=True, verbose_name='Видео')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объявление о наборе студентов'
        verbose_name_plural = 'Объявления о наборе студентов'
        ordering = ('-created_at',)


class RecruitmentAnnouncementFile(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    link = models.FileField(upload_to='recruitment_file', max_length=255, verbose_name='Путь к файлу')
    recruitment_announcement = models.ForeignKey(
        RecruitmentAnnouncement,
        on_delete=models.CASCADE,
        related_name='recruitment_file',
        verbose_name='Объявление о наборе'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Файл объявления'
        verbose_name_plural = 'Файлы объявлений'
        db_table = 'recruitment_file'
