from django.urls import path

from apps.center_courses.views import CenterCourseInfoLatestObjectRetrieveAPIView, \
    LessonInfoLatestObjectRetrieveAPIView, LessonMaterialListAPIView, CenterCourseBannerRetrieveAPIView

urlpatterns = [
    path('courses/banner/', CenterCourseBannerRetrieveAPIView.as_view(), name='course_info_banner'),
    path('courses/course-info/', CenterCourseInfoLatestObjectRetrieveAPIView.as_view(), name='course_info'),
    path('courses/lesson/', LessonInfoLatestObjectRetrieveAPIView.as_view(), name='lesson'),
    path('courses/material/', LessonMaterialListAPIView.as_view(), name='material'),
]
