from modeltranslation.translator import register, TranslationOptions

from apps.library.models import Gallery, EducationalMaterial


@register(Gallery)
class GalleryTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(EducationalMaterial)
class EducationalMaterialTranslationOptions(TranslationOptions):
    fields = ('title',)
