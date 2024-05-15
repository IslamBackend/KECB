from rest_framework.generics import ListAPIView

from apps.center_info.models import DirectorSpeech, CenterHistory, CenterActivity
from apps.center_info.serializers import DirectorSpeachSerializer, CenterHistorySerializer, CenterActivitySerializer
from apps.common.views import LatestObjectRetrieveAPIView


class DirectorSpeechRetrieveAPIView(LatestObjectRetrieveAPIView):
    model = DirectorSpeech
    serializer_class = DirectorSpeachSerializer


class CenterHistoryListAPIView(ListAPIView):
    queryset = CenterHistory.objects.all()
    serializer_class = CenterHistorySerializer


class BaseCenterActivityListView(ListAPIView):
    serializer_class = CenterActivitySerializer
    activity_type = None

    def get_queryset(self):
        return CenterActivity.objects.filter(activity_type=self.activity_type)


class KoreanLanguageActivityListAPIView(BaseCenterActivityListView):
    activity_type = 'Распространение корейского языка'


class StudentsSupportActivityListAPIView(BaseCenterActivityListView):
    activity_type = 'Деятельность по поддержке иностранных студентов'
