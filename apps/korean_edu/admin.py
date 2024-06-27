from django.contrib import admin
from django_summernote import admin as sadmin
from modeltranslation.admin import TranslationAdmin

from apps.korean_edu.models import UniversityInfo, RecruitmentAnnouncement, RecruitmentAnnouncementFile


@admin.register(UniversityInfo)
class UniversityInfoAdmin(sadmin.SummernoteModelAdmin, TranslationAdmin):
    list_display = ('title', 'type', 'founding_year')
    search_fields = ('title',)


class RecruitmentAnnouncementFileAdmin(admin.TabularInline):
    fields = ('title_ru', 'title_ko', 'link')
    model = RecruitmentAnnouncementFile


@admin.register(RecruitmentAnnouncement)
class AnnouncementAdmin(sadmin.SummernoteModelAdmin, TranslationAdmin):
    list_display = ('title_ru', 'created_at')
    summernote_fields = ('description',)
    search_fields = ('title_ru', 'description')
    inlines = [RecruitmentAnnouncementFileAdmin]
