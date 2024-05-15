from rest_framework import serializers

from apps.center_courses.models import CenterCourseInfo, CenterCourseInfoImage, LessonInfo, LessonInfoImage, \
    LessonMaterial


class CenterCourseInfoImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CenterCourseInfoImage
        fields = ('id', 'image')


class CenterCourseInfoSerializer(serializers.ModelSerializer):
    course_images = CenterCourseInfoImageSerializer(many=True)

    class Meta:
        model = CenterCourseInfo
        fields = ('id', 'title', 'description', 'video', 'course_images')


class LessonInfoImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonInfoImage
        fields = ('id', 'image')


class LessonInfoSerializer(serializers.ModelSerializer):
    lesson_images = LessonInfoImageSerializer(many=True)

    class Meta:
        model = LessonInfo
        fields = ('id', 'title', 'description', 'video', 'lesson_images')


class LessonMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonMaterial
        fields = ('id', 'title', 'file_path')
