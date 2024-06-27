from django.contrib import admin

from django_summernote import admin as sadmin
from modeltranslation.admin import TranslationAdmin

from apps.center_info.models import DirectorSpeech, CenterHistory, CenterActivityImage, CenterActivity, QuestionAnswer


@admin.register(DirectorSpeech)
class DirectorSpeechAdmin(sadmin.SummernoteModelAdmin, TranslationAdmin):
    list_display = ('text_ru', 'text_ko')
    summernote_fields = ('text_ru', 'text_ko')

    def has_add_permission(self, request):
        return not DirectorSpeech.objects.exists()

    def has_change_permission(self, request, obj=None):
        return DirectorSpeech.objects.exists()


@admin.register(CenterHistory)
class CenterHistoryAdmin(sadmin.SummernoteModelAdmin, TranslationAdmin):
    list_display = ('title_ru', 'title_ko')
    search_fields = ('title_ru', 'title_ko')


class CenterActivityImageAdmin(admin.TabularInline):
    model = CenterActivityImage


@admin.register(CenterActivity)
class CenterActivityAdmin(sadmin.SummernoteModelAdmin, TranslationAdmin):
    list_display = ('title_ru', 'title_ko')
    summernote_fields = ('description_ru', 'description_ko')
    search_fields = ('title_ru', 'description_ru')
    inlines = [CenterActivityImageAdmin, ]


@admin.register(QuestionAnswer)
class CenterActivityAdmin(TranslationAdmin):
    list_display = ('question_ru', 'question_ko',)
    search_fields = ('question_ru', 'question_ko')
