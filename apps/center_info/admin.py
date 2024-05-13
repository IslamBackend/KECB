from django.contrib import admin

from django_summernote import admin as sadmin

from apps.center_info.models import DirectorSpeech, CenterHistory, CenterActivityImage, CenterActivity


@admin.register(DirectorSpeech)
class DirectorSpeechAdmin(sadmin.SummernoteModelAdmin):
    list_display = ('text',)
    summernote_fields = ('text',)

    def has_add_permission(self, request):
        return not DirectorSpeech.objects.exists()

    def has_change_permission(self, request, obj=None):
        return DirectorSpeech.objects.exists()


@admin.register(CenterHistory)
class CenterHistoryAdmin(sadmin.SummernoteModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'description')


class CenterActivityImageAdmin(admin.TabularInline):
    model = CenterActivityImage


@admin.register(CenterActivity)
class CenterActivityAdmin(sadmin.SummernoteModelAdmin):
    list_display = ('title', 'activity_type')
    summernote_fields = ('description',)
    search_fields = ('title', 'description')
    inlines = [CenterActivityImageAdmin, ]
