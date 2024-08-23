from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
import factory

from apps.center_courses.models import CourseOrLessonInfo, CourseOrLessonImage


class CourseOrLessonInfoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CourseOrLessonInfo

    title = factory.Faker('word')
    description = factory.Faker('sentence', nb_words=3)
    video = factory.Faker('url')
    type = factory.Iterator([choice[0] for choice in CourseOrLessonInfo.TITLE_CHOICES])


class CourseOrLessonImageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CourseOrLessonImage

    image = factory.django.ImageField(filename='test_image.jpg')
    info = factory.SubFactory(CourseOrLessonInfoFactory)


class CenterCoursesInfoTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.course_info = CourseOrLessonInfoFactory(type='course')
        self.course_image = CourseOrLessonImageFactory(info=self.course_info)
        self.lesson_info = CourseOrLessonInfoFactory(type='lesson')
        self.lesson_image = CourseOrLessonImageFactory(info=self.lesson_info)

    def get_expected_info_data(self, info, image):
        return {
            'id': info.id,
            'title': info.title,
            'description': info.description,
            'video': info.video,
            'type': info.type,
            'images': [
                {
                    'id': image.id,
                    'image': f'http://testserver/media/{image.image}',
                }
            ]
        }

    def test_course_info(self):
        response = self.client.get(reverse('course_info'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_data = self.get_expected_info_data(self.course_info, self.course_image)
        actual_data = response.json()

        self.assertEqual(actual_data, expected_data)
        self.assertEqual(len(actual_data['images']), 1)

    def test_lesson_info(self):
        response = self.client.get(reverse('lesson'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_data = self.get_expected_info_data(self.lesson_info, self.lesson_image)
        actual_data = response.json()

        self.assertEqual(actual_data, expected_data)
        self.assertEqual(len(actual_data['images']), 1)
