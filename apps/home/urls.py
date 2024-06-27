from django.urls import path

from apps.home.views import HomeBannerRetrieveAPIView, HomeAnnouncementListAPIView, HomeGalleryListAPIView, \
    SocialInfoLatestObjectRetrieveAPIView, KoreanSiteListAPIView

urlpatterns = [
    path('social-info/', SocialInfoLatestObjectRetrieveAPIView.as_view(), name='social_info'),
    path('home/banner/', HomeBannerRetrieveAPIView.as_view(), name='home_banner'),
    path('home/announcement/', HomeAnnouncementListAPIView.as_view(), name='home_announcement'),
    path('home/gallery/', HomeGalleryListAPIView.as_view(), name='home_gallery'),
    path('home/korean-site/', KoreanSiteListAPIView.as_view(), name='korean_site'),
]
