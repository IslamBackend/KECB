from modeltranslation.translator import register, TranslationOptions

from apps.korean_edu.models import UniversityInfo, RecruitmentAnnouncement, RecruitmentAnnouncementFile


@register(UniversityInfo)
class BannerTranslationOptions(TranslationOptions):
    fields = ('title', 'address')


@register(RecruitmentAnnouncement)
class RecruitmentAnnouncementTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(RecruitmentAnnouncementFile)
class RecruitmentAnnouncementFileTranslationOptions(TranslationOptions):
    fields = ('title',)
