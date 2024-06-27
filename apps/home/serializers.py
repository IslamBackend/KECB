from rest_framework import serializers

from apps.home.models import Banner, SocialInfo, KoreanSite


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ('id', 'title', 'description', 'image')


class SocialInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialInfo
        fields = (
            'id', 'image', 'phone_number_first', 'phone_number_second', 'email', 'working_hours',
            'longitude', 'latitude', 'telegram_url', 'whatsapp_url_first', 'whatsapp_url_second',
            'instagram_url', 'youtube_url', 'facebook_url', 'twitter_url'
        )


class KoreanSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = KoreanSite
        fields = ('id', 'name', 'logo', 'url')
