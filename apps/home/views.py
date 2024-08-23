from django.db.models import Q
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from apps.announcement.models import Announcement
from apps.announcement.serializers import AnnouncementSerializer
from apps.common.views import LatestBannerRetrieveAPIView, LatestObjectRetrieveAPIView
from apps.home.models import SocialInfo, KoreanSite
from apps.home.serializers import SocialInfoSerializer, KoreanSiteSerializer
from apps.library.models import Gallery
from apps.library.serializers import GallerySerializer


class HomeBannerRetrieveAPIView(LatestBannerRetrieveAPIView):
    page = 'Главная'


class HomeAnnouncementListAPIView(ListAPIView):
    serializer_class = AnnouncementSerializer

    def get_queryset(self):
        return Announcement.objects.select_related('rubric').order_by('-created_at')[:6]


class HomeGalleryListAPIView(ListAPIView):
    serializer_class = GallerySerializer

    def get_queryset(self):
        return Gallery.objects.order_by('-created_at')[:6]


class SocialInfoLatestObjectRetrieveAPIView(LatestObjectRetrieveAPIView):
    model = SocialInfo
    serializer_class = SocialInfoSerializer


class KoreanSiteListAPIView(ListAPIView):
    queryset = KoreanSite.objects.all()
    serializer_class = KoreanSiteSerializer


class SearchListAPIView(ListAPIView):
    def get(self, request, *args, **kwargs):
        q = request.query_params.get('q', '')
        results = {
            'announcements': [],
            'galleries': []
        }

        if q:
            announcement_results = Announcement.objects.filter(
                Q(title__icontains=q) |
                Q(description__icontains=q)
            ).values('id', 'title')

            gallery_results = Gallery.objects.filter(
                Q(title__icontains=q) |
                Q(description__icontains=q)
            ).values('id', 'title')

            results['announcements'] = list(announcement_results)
            results['galleries'] = list(gallery_results)

        return Response(results)
