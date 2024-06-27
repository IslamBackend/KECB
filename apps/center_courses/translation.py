from modeltranslation.translator import register, TranslationOptions

from apps.center_courses.models import CenterCourseInfo, LessonInfo, LessonMaterial


@register(CenterCourseInfo)
class BaseInfoTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(LessonInfo)
class LessonInfoTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(LessonMaterial)
class LessonMaterialTranslationOptions(TranslationOptions):
    fields = ('title',)
