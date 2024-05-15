from rest_framework.generics import ListAPIView, RetrieveAPIView

from apps.korean_edu.models import UniversityInfo, RecruitmentAnnouncement
from apps.korean_edu.serializers import UniversityInfoSerializer, RecruitmentAnnouncementSerializer, \
    RecruitmentAnnouncementDetailSerializer


class UniversityInfoListAPIView(ListAPIView):
    queryset = UniversityInfo.objects.all()
    serializer_class = UniversityInfoSerializer


class RecruitmentAnnouncementListAPIView(ListAPIView):
    queryset = RecruitmentAnnouncement.objects.all()
    serializer_class = RecruitmentAnnouncementSerializer


class RecruitmentAnnouncementRetrieveAPIView(RetrieveAPIView):
    queryset = RecruitmentAnnouncement.objects.all()
    serializer_class = RecruitmentAnnouncementDetailSerializer
