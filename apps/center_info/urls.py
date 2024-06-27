from django.urls import path

from apps.center_info.views import DirectorSpeechRetrieveAPIView, CenterHistoryListAPIView, \
    KoreanLanguageActivityListAPIView, StudentsSupportActivityListAPIView, QuestionAnswerListAPIView, \
    CenterInfoBannerRetrieveAPIView, QuestionAnswerBannerRetrieveAPIView

urlpatterns = [
    path('center_info/banner/', CenterInfoBannerRetrieveAPIView.as_view(), name='center_info_banner'),
    path('center_info/speech/', DirectorSpeechRetrieveAPIView.as_view(), name='center_info_speech'),
    path('center_info/history/', CenterHistoryListAPIView.as_view(), name='center_info_history'),
    path('activity/distribution/', KoreanLanguageActivityListAPIView.as_view(), name='activity_distribution'),
    path('activity/support/', StudentsSupportActivityListAPIView.as_view(), name='activity_support'),
    path('faq/banner/', QuestionAnswerBannerRetrieveAPIView.as_view(), name='faq_banner'),
    path('faq/', QuestionAnswerListAPIView.as_view(), name='faq'),
]
