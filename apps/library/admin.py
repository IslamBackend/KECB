from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from apps.library.models import Gallery, GalleryImage, EducationalMaterial


class GalleryImageAdmin(admin.TabularInline):
    model = GalleryImage


@admin.register(Gallery)
class GalleryAdmin(TranslationAdmin):
    list_display = ('title_ru', 'title_ko', 'created_at')
    search_fields = ('title_ru', 'title_ko', 'description')
    inlines = [GalleryImageAdmin]


@admin.register(EducationalMaterial)
class EducationalMaterialAdmin(TranslationAdmin):
    list_display = ('title_ru', 'title_ko', 'link')
    search_fields = ('title_ru', 'title_ko')
