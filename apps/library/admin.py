from django.contrib import admin

from apps.library.models import Gallery, GalleryImage, EducationalMaterial


class GalleryImageAdmin(admin.TabularInline):
    model = GalleryImage


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'rubric', 'created_at')
    search_fields = ('title', 'description')
    inlines = [GalleryImageAdmin]


@admin.register(EducationalMaterial)
class EducationalMaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'link')
    search_fields = ('title',)
