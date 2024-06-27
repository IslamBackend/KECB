from modeltranslation.translator import register, TranslationOptions

from apps.announcement.models import Rubric, Announcement


@register(Rubric)
class RubricTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Announcement)
class AnnouncementTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
