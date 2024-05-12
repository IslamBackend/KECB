from rest_framework import serializers

from apps.announcement.models import Announcement, AnnouncementFile, AnnouncementVideo, AnnouncementImage


class AnnouncementSerializer(serializers.ModelSerializer):
    rubric = serializers.StringRelatedField()

    class Meta:
        model = Announcement
        fields = ('id', 'image', 'title', 'rubric', 'created_at')


class AnnouncementFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnouncementFile
        fields = ('id', 'title', 'file_path')


class AnnouncementVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnouncementVideo
        fields = ('id', 'link')


class AnnouncementImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnouncementImage
        fields = ('id', 'image')


class AnnouncementDetailSerializer(serializers.ModelSerializer):
    rubric = serializers.StringRelatedField()
    files = AnnouncementFileSerializer(many=True)
    videos = AnnouncementVideoSerializer(many=True)
    images = AnnouncementImageSerializer(many=True)

    class Meta:
        model = Announcement
        fields = ('id', 'image', 'title', 'rubric', 'description', 'images', 'videos', 'files', 'created_at')
