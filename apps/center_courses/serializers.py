from rest_framework import serializers

from apps.center_courses.models import CourseOrLessonInfo, CourseOrLessonImage, LessonMaterial


class CourseOrLessonImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseOrLessonImage
        fields = ('id', 'image')


class CourseOrLessonInfoSerializer(serializers.ModelSerializer):
    images = CourseOrLessonImageSerializer(many=True)

    class Meta:
        model = CourseOrLessonInfo
        fields = ('id', 'title', 'description', 'video', 'type', 'images')


class LessonMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonMaterial
        fields = ('id', 'title', 'file_path')
