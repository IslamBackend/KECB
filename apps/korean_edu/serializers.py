from rest_framework import serializers

from apps.korean_edu.models import UniversityInfo, RecruitmentAnnouncement, RecruitmentAnnouncementFile


class UniversityInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityInfo
        fields = ('id', 'title', 'type', 'address', 'founding_year', 'website')


class RecruitmentAnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecruitmentAnnouncement
        fields = ('id', 'title', 'created_at')


class RecruitmentAnnouncementFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecruitmentAnnouncementFile
        fields = ('id', 'title', 'file_path')


class RecruitmentAnnouncementDetailSerializer(serializers.ModelSerializer):
    recruitment_file = RecruitmentAnnouncementFileSerializer(many=True)

    class Meta:
        model = RecruitmentAnnouncement
        fields = ('id', 'title', 'description', 'created_at', 'recruitment_file')
