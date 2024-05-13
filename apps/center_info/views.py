from rest_framework.generics import ListAPIView, RetrieveAPIView

from apps.center_info.models import DirectorSpeech, CenterHistory, CenterActivity
from apps.center_info.serializers import DirectorSpeachSerializer, CenterHistorySerializer, CenterActivitySerializer


class DirectorSpeechRetrieveAPIView(RetrieveAPIView):
    serializer_class = DirectorSpeachSerializer

    def get_object(self):
        return DirectorSpeech.objects.latest('id')


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
