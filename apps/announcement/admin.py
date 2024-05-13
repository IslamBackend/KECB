from django.contrib import admin

from django_summernote import admin as sadmin

from apps.announcement.models import Announcement, AnnouncementFile, AnnouncementImage, AnnouncementVideo, Rubric


class AnnouncementFileAdmin(admin.TabularInline):
    model = AnnouncementFile


class AnnouncementImageAdmin(admin.TabularInline):
    model = AnnouncementImage


class AnnouncementVideoFileAdmin(admin.TabularInline):
    model = AnnouncementVideo


@admin.register(Rubric)
class RubricAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Announcement)
class AnnouncementAdmin(sadmin.SummernoteModelAdmin):
    list_display = ('title', 'rubric', 'created_at')
    summernote_fields = ('description',)
    search_fields = ('title', 'description')
    inlines = [AnnouncementFileAdmin, AnnouncementImageAdmin, AnnouncementVideoFileAdmin]


