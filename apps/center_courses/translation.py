from modeltranslation.translator import register, TranslationOptions

from apps.center_courses.models import CourseOrLessonInfo, LessonMaterial


@register(CourseOrLessonInfo)
class BaseInfoTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(LessonMaterial)
class LessonMaterialTranslationOptions(TranslationOptions):
    fields = ('title',)
