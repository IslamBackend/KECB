from django.contrib import admin
from django_summernote import admin as sadmin
from modeltranslation.admin import TranslationAdmin

from apps.center_courses.models import CenterCourseInfo, CenterCourseInfoImage, LessonInfo, LessonInfoImage, \
    LessonMaterial


class BaseInlineAdmin(admin.TabularInline):
    min_num = 0
    max_num = 3
    extra = 1
    show_change_link = True


class CenterCourseInfoImageAdmin(BaseInlineAdmin):
    model = CenterCourseInfoImage


class LessonInfoImageAdmin(BaseInlineAdmin):
    model = LessonInfoImage


@admin.register(CenterCourseInfo)
class CenterCourseInfoAdmin(sadmin.SummernoteModelAdmin, TranslationAdmin):
    list_display = ('title_ru',)
    summernote_fields = ('description_ru', 'description_ko')
    inlines = [CenterCourseInfoImageAdmin, ]


@admin.register(LessonInfo)
class LessonInfoAdmin(sadmin.SummernoteModelAdmin, TranslationAdmin):
    list_display = ('title_ru',)
    summernote_fields = ('description_ru', 'description_ko')
    inlines = [LessonInfoImageAdmin, ]


@admin.register(LessonMaterial)
class LessonMaterialAdmin(sadmin.SummernoteModelAdmin, TranslationAdmin):
    list_display = ('title_ru', 'file_path')
