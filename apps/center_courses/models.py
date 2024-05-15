from django.db import models


class BaseInfo(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    video = models.URLField(null=True, blank=True, verbose_name='Видео')

    class Meta:
        abstract = True


class CenterCourseInfo(BaseInfo):
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Информация о курсе центра'
        verbose_name_plural = 'Информация о курсах центра'
        db_table = 'center_course_info'


class CenterCourseInfoImage(models.Model):
    image = models.ImageField(upload_to='course_image', verbose_name='Изображение')
    course_info = models.ForeignKey(
        CenterCourseInfo,
        on_delete=models.CASCADE,
        related_name='course_images',
        verbose_name='Курс центра'
    )

    class Meta:
        verbose_name = 'Изображение курса центра'
        verbose_name_plural = 'Изображения курсов центра'
        db_table = 'center_course_info_image'


class LessonInfo(BaseInfo):
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Информация о занятии'
        verbose_name_plural = 'Информация о занятиях'
        db_table = 'lesson_info'


class LessonInfoImage(models.Model):
    image = models.ImageField(upload_to='lesson_image', verbose_name='Изображение')
    lesson_info = models.ForeignKey(
        LessonInfo,
        on_delete=models.CASCADE,
        related_name='lesson_images',
        verbose_name='Информация о занятии'
    )

    class Meta:
        verbose_name = 'Изображение занятия'
        verbose_name_plural = 'Изображения занятий'
        db_table = 'lesson_info_image'


class LessonMaterial(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    file_path = models.FileField(upload_to='lesson_material', max_length=255, verbose_name='Путь к файлу')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Материал для урока'
        verbose_name_plural = 'Материалы для уроков'
        ordering = ['-id']
        db_table = 'lesson_material'
