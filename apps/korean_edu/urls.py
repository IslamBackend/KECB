from django.urls import path

from apps.korean_edu.views import UniversityInfoListAPIView, RecruitmentAnnouncementListAPIView, \
    RecruitmentAnnouncementRetrieveAPIView, KoreanEduBannerRetrieveAPIView

urlpatterns = [
    path('education/banner/', KoreanEduBannerRetrieveAPIView.as_view(), name='university_banner'),
    path('education/info/', UniversityInfoListAPIView.as_view(), name='university_info'),
    path('education/recruitment/', RecruitmentAnnouncementListAPIView.as_view(), name='recruitment'),
    path('education/recruitment/<int:pk>/', RecruitmentAnnouncementRetrieveAPIView.as_view(), name='recruitment_detail'),
]
