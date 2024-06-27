from modeltranslation.translator import register, TranslationOptions

from apps.home.models import Banner, SocialInfo, KoreanSite


@register(Banner)
class BannerTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(SocialInfo)
class SocialInfoTranslationOptions(TranslationOptions):
    fields = ('working_hours',)


@register(KoreanSite)
class KoreanSiteTranslationOptions(TranslationOptions):
    fields = ('name',)
