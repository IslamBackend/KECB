from rest_framework.generics import ListAPIView

from apps.center_courses.models import CenterCourseInfo, LessonInfo, LessonMaterial
from apps.center_courses.serializers import CenterCourseInfoSerializer, LessonInfoSerializer, LessonMaterialSerializer
from apps.common.views import LatestObjectRetrieveAPIView


class CenterCourseInfoLatestObjectRetrieveAPIView(LatestObjectRetrieveAPIView):
    model = CenterCourseInfo
    serializer_class = CenterCourseInfoSerializer


class LessonInfoLatestObjectRetrieveAPIView(LatestObjectRetrieveAPIView):
    model = LessonInfo
    serializer_class = LessonInfoSerializer


class LessonMaterialListAPIView(ListAPIView):
    queryset = LessonMaterial.objects.all()
    serializer_class = LessonMaterialSerializer
