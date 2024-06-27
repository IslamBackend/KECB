from django.urls import path

from apps.announcement.views import AnnouncementListAPIView, AnnouncementDetailAPIView, \
    AnnouncementBannerRetrieveAPIView

urlpatterns = [
    path('announcement/banner/', AnnouncementBannerRetrieveAPIView.as_view(), name='announcement_banner'),
    path('announcement/', AnnouncementListAPIView.as_view(), name='announcement_list'),
    path('announcement/<int:pk>/', AnnouncementDetailAPIView.as_view(), name='announcement_detail')
]
