from rest_framework.generics import ListAPIView

from apps.center_courses.models import CourseOrLessonInfo, LessonMaterial
from apps.center_courses.serializers import CourseOrLessonInfoSerializer, LessonMaterialSerializer
from apps.common.views import LatestObjectRetrieveAPIView, LatestBannerRetrieveAPIView


class CenterCourseBannerRetrieveAPIView(LatestBannerRetrieveAPIView):
    page = 'Курсы центра'


class CenterCourseInfoLatestObjectRetrieveAPIView(LatestObjectRetrieveAPIView):
    model = CourseOrLessonInfo
    serializer_class = CourseOrLessonInfoSerializer
    type = 'course'


class LessonInfoLatestObjectRetrieveAPIView(LatestObjectRetrieveAPIView):
    model = CourseOrLessonInfo
    serializer_class = CourseOrLessonInfoSerializer
    type = 'lesson'


class LessonMaterialListAPIView(ListAPIView):
    queryset = LessonMaterial.objects.all()
    serializer_class = LessonMaterialSerializer
