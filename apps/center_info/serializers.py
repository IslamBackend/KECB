from rest_framework import serializers

from apps.center_info.models import DirectorSpeech, CenterHistory, CenterActivity, CenterActivityImage, QuestionAnswer


class DirectorSpeachSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectorSpeech
        fields = ('id', 'image', 'text')


class CenterHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CenterHistory
        fields = ('id', 'title', 'image', 'description', 'date')


class CenterActivityImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CenterActivityImage
        fields = ('id', 'image')


class CenterActivitySerializer(serializers.ModelSerializer):
    center_activity_images = CenterActivityImageSerializer(many=True)

    class Meta:
        model = CenterActivity
        fields = ('id', 'title', 'description', 'video', 'center_activity_images')


class QuestionAnswerSerializer(serializers.ModelSerializer):
    rubric = serializers.StringRelatedField()

    class Meta:
        model = QuestionAnswer
        fields = ('id', 'rubric', 'question', 'answer')
