from modeltranslation.translator import register, TranslationOptions

from apps.center_info.models import DirectorSpeech, CenterHistory, CenterActivity, QuestionAnswer


@register(DirectorSpeech)
class DirectorSpeechTranslationOptions(TranslationOptions):
    fields = ('text', )


@register(CenterHistory)
class CenterHistoryTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(CenterActivity)
class CenterActivityTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(QuestionAnswer)
class QuestionAnswerTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')
