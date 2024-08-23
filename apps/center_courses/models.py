from django.db import models


class CourseOrLessonInfo(models.Model):
    TITLE_CHOICES = [
        ('course', 'Информация о курсе центра'),
        ('lesson', 'Информация о занятии'),
    ]

    title = models.CharField(max_length=125, verbose_name='Заголовок')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    video = models.URLField(null=True, blank=True, verbose_name='Видео')
    type = models.CharField(max_length=10, choices=TITLE_CHOICES, verbose_name='Тип')

    def __str__(self):
        type_display = dict(self.TITLE_CHOICES).get(self.type)
        return f"{self.title} ({type_display})"

    class Meta:
        verbose_name = 'Информация'
        verbose_name_plural = 'Информация'
        db_table = 'course_or_lesson_info'


class CourseOrLessonImage(models.Model):
    image = models.ImageField(upload_to='info_images', verbose_name='Изображение')
    info = models.ForeignKey(
        CourseOrLessonInfo,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Информация'
    )

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        db_table = 'course_or_lesson_info_image'


class LessonMaterial(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    file_path = models.FileField(upload_to='lesson_material', max_length=255, verbose_name='Путь к файлу')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Материал для урока'
        verbose_name_plural = 'Материалы для уроков'
        ordering = ('-id',)
        db_table = 'lesson_material'
