from django.contrib import admin

from django_summernote import admin as sadmin
from modeltranslation.admin import TranslationAdmin

from apps.announcement.models import Announcement, AnnouncementFile, AnnouncementImage, AnnouncementVideo, Rubric


class AnnouncementFileAdmin(admin.TabularInline):
    model = AnnouncementFile


class AnnouncementImageAdmin(admin.TabularInline):
    model = AnnouncementImage


class AnnouncementVideoFileAdmin(admin.TabularInline):
    model = AnnouncementVideo


@admin.register(Rubric)
class RubricAdmin(TranslationAdmin):
    list_display = ('title', 'title_ko')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Announcement)
class AnnouncementAdmin(sadmin.SummernoteModelAdmin, TranslationAdmin):
    list_display = ('title_ru', 'rubric', 'created_at')
    summernote_fields = ('description_ru', 'description_ko')
    search_fields = ('title_ru', 'description_ru')
    inlines = [AnnouncementFileAdmin, AnnouncementImageAdmin, AnnouncementVideoFileAdmin]


