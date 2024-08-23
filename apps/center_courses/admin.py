from django.contrib import admin
from django_summernote import admin as sadmin
from modeltranslation.admin import TranslationAdmin

from apps.center_courses.models import CourseOrLessonInfo, CourseOrLessonImage, LessonMaterial


class BaseInlineAdmin(admin.TabularInline):
    min_num = 0
    max_num = 3
    extra = 1
    show_change_link = True


class CourseOrLessonImageAdmin(BaseInlineAdmin):
    model = CourseOrLessonImage


@admin.register(CourseOrLessonInfo)
class CenterCourseInfoAdmin(sadmin.SummernoteModelAdmin, TranslationAdmin):
    summernote_fields = ('description_ru', 'description_ko')
    inlines = [CourseOrLessonImageAdmin, ]


@admin.register(LessonMaterial)
class LessonMaterialAdmin(sadmin.SummernoteModelAdmin, TranslationAdmin):
    list_display = ('title_ru', 'file_path')
