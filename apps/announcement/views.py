from rest_framework.generics import ListAPIView, RetrieveAPIView

from apps.announcement.models import Announcement
from apps.announcement.pagination import CustomPagination
from apps.announcement.serializers import AnnouncementSerializer, AnnouncementDetailSerializer
from apps.common.views import LatestBannerRetrieveAPIView


class AnnouncementBannerRetrieveAPIView(LatestBannerRetrieveAPIView):
    page = 'Объявления'


class AnnouncementListAPIView(ListAPIView):
    queryset = Announcement.objects.select_related('rubric')
    serializer_class = AnnouncementSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = self.queryset
        rubric = self.request.query_params.get('rubric', None)
        if rubric is not None:
            queryset = queryset.filter(rubric__title=rubric)
        return queryset


class AnnouncementDetailAPIView(RetrieveAPIView):
    queryset = Announcement.objects.select_related('rubric')
    serializer_class = AnnouncementDetailSerializer
