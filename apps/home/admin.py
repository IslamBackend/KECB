from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from apps.home.models import Banner, SocialInfo, KoreanSite


@admin.register(Banner)
class BannerAdmin(TranslationAdmin):
    list_display = ('title_ru', 'title_ko')


@admin.register(SocialInfo)
class SocialInfoAdmin(TranslationAdmin):
    list_display = ('working_hours_ru',)

    def has_add_permission(self, request):
        return not SocialInfo.objects.exists()


@admin.register(KoreanSite)
class KoreanSiteAdmin(TranslationAdmin):
    list_display = ('name', 'url', 'logo')
    fields = ('name', 'url', 'logo')
