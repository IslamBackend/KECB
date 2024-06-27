from rest_framework.generics import ListAPIView

from apps.center_info.models import DirectorSpeech, CenterHistory, CenterActivity, QuestionAnswer
from apps.center_info.serializers import DirectorSpeachSerializer, CenterHistorySerializer, CenterActivitySerializer, \
    QuestionAnswerSerializer
from apps.common.views import LatestObjectRetrieveAPIView, LatestBannerRetrieveAPIView


class CenterInfoBannerRetrieveAPIView(LatestBannerRetrieveAPIView):
    page = 'О центре'


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


class QuestionAnswerBannerRetrieveAPIView(LatestBannerRetrieveAPIView):
    page = 'Q&A'


class QuestionAnswerListAPIView(ListAPIView):
    serializer_class = QuestionAnswerSerializer

    def get_queryset(self):
        queryset = QuestionAnswer.objects.all()
        rubric = self.request.query_params.get('rubric', None)
        if rubric is not None:
            queryset = queryset.filter(rubric__title=rubric)
        return queryset
