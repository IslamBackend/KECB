from django.urls import path

from apps.center_info.views import DirectorSpeechRetrieveAPIView, CenterHistoryListAPIView, \
    KoreanLanguageActivityListAPIView, StudentsSupportActivityListAPIView

urlpatterns = [
    path('center_info/speech/', DirectorSpeechRetrieveAPIView.as_view(), name='center_info_speech'),
    path('center_info/history/', CenterHistoryListAPIView.as_view(), name='center_info_history'),
    path('activity/distribution/', KoreanLanguageActivityListAPIView.as_view(), name='activity_distribution'),
    path('activity/support/', StudentsSupportActivityListAPIView.as_view(), name='activity_support'),
]
