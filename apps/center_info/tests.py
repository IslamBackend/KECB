import factory
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from apps.announcement.models import Rubric
from apps.center_info.constants import ACTIVITY_CHOICES
from apps.center_info.models import DirectorSpeech, CenterHistory, CenterActivity, CenterActivityImage, QuestionAnswer


class DirectorSpeechFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = DirectorSpeech

    text = factory.Faker('text', max_nb_chars=200)
    image = factory.django.ImageField(filename='test_image.jpg')


class DirectorSpeechTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.director_speech = DirectorSpeechFactory()

    def get_expected_director_speech(self):
        return {
            'id': self.director_speech.id,
            'text': self.director_speech.text,
            'image': f'http://testserver/media/{self.director_speech.image}',
        }

    def test_director_speech_list(self):
        response = self.client.get(reverse('center_info_speech'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), self.get_expected_director_speech())


class CenterHistoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CenterHistory

    title = factory.Faker('sentence', nb_words=3)
    description = factory.Faker('text', max_nb_chars=10)
    image = factory.django.ImageField(filename='test_image.jpg')
    date = factory.Faker('date_this_decade')


class CenterHistoryTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.center_history = CenterHistoryFactory()

    def get_expected_center_history(self):
        return {
            'id': self.center_history.id,
            'title': self.center_history.title,
            'description': self.center_history.description,
            'image': f'http://testserver/media/{self.center_history.image}',
            'date': self.center_history.date.strftime('%d.%m.%Y')  # Форматируем дату
        }

    def test_center_history_list(self):
        response = self.client.get(reverse('center_info_history'))
        self.assertTrue(CenterHistory.objects.exists())
        self.assertEqual(len(response.data), 1)
        self.assertIn(self.get_expected_center_history(), response.data)


class CenterActivityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CenterActivity

    title = factory.Faker('sentence', nb_words=3)
    activity_type = factory.Iterator([choice[0] for choice in ACTIVITY_CHOICES])
    description = factory.Faker('text', max_nb_chars=10)
    video = factory.Faker('url')


class CenterActivityImageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CenterActivityImage

    image = factory.django.ImageField(filename='test_image.jpg')
    center_activity = factory.SubFactory(CenterActivityFactory)


class CenterActivityTests(APITestCase):
    def setUp(self):
        self.client = APIClient()

        self.activity_distribution = CenterActivityFactory(activity_type='Распространение корейского языка')
        self.activity_support = CenterActivityFactory(activity_type='Деятельность по поддержке иностранных студентов')

        self.activity_distribution_image = CenterActivityImageFactory(center_activity=self.activity_distribution)
        self.activity_support_image = CenterActivityImageFactory(center_activity=self.activity_support)

    def get_expected_center_activity(self, center_activity, center_activity_image):
        return {
            'id': center_activity.id,
            'title': center_activity.title,
            'description': center_activity.description,
            'video': center_activity.video,
            'center_activity_images': [
                {
                    'id': center_activity_image.id,
                    'image': f'http://testserver/media/{center_activity_image.image}',
                }
            ]
        }

    def test_activity_distribution(self):
        response = self.client.get(reverse('activity_distribution'))
        expected_data = self.get_expected_center_activity(self.activity_distribution, self.activity_distribution_image)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(expected_data, response.data)
        self.assertEqual(len(response.data), 1)

    def test_activity_support(self):
        response = self.client.get(reverse('activity_support'))
        expected_data = self.get_expected_center_activity(self.activity_support, self.activity_support_image)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(expected_data, response.data)
        self.assertEqual(len(response.data), 1)


class RubricFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Rubric

    title = factory.Faker('word')


class QuestionAnswerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = QuestionAnswer

    question = factory.Faker('sentence', nb_words=3)
    answer = factory.Faker('sentence', nb_words=3)
    rubric = factory.SubFactory(RubricFactory)


class QuestionAnswerTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.rubric = RubricFactory()
        self.question_answer = QuestionAnswerFactory(rubric=self.rubric)

    def expected_data(self):
        return {
            'id': self.question_answer.id,
            'rubric': self.rubric.title,
            'question': self.question_answer.question,
            'answer': self.question_answer.answer,
        }

    def test_question_answer(self):
        response = self.client.get(reverse('faq'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0], self.expected_data())
        self.assertEqual(len(response.data), 1)
