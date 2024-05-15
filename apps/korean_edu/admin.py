from django.contrib import admin
from django_summernote import admin as sadmin

from apps.korean_edu.models import UniversityInfo, RecruitmentAnnouncement, RecruitmentAnnouncementFile


@admin.register(UniversityInfo)
class UniversityInfoAdmin(sadmin.SummernoteModelAdmin):
    list_display = ('title', 'type', 'founding_year')
    search_fields = ('title',)


class RecruitmentAnnouncementFileAdmin(admin.TabularInline):
    model = RecruitmentAnnouncementFile


@admin.register(RecruitmentAnnouncement)
class AnnouncementAdmin(sadmin.SummernoteModelAdmin):
    list_display = ('title', 'created_at')
    summernote_fields = ('description',)
    search_fields = ('title', 'description')
    inlines = [RecruitmentAnnouncementFileAdmin]
