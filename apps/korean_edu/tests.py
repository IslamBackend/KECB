import factory
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from apps.korean_edu.models import UniversityInfo, RecruitmentAnnouncement, RecruitmentAnnouncementFile


class UniversityInfoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UniversityInfo

    title = factory.Faker('company')
    image = factory.django.ImageField(filename='test_image.jpg')
    type = factory.Iterator(['Type1', 'Type2'])
    address = factory.Faker('address')
    founding_year = factory.Faker('year')
    website = factory.Faker('url')


class UniversityInfoTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.universities = UniversityInfoFactory.create_batch(3)
        self.url = reverse('university_info')

    def expected_data(self):
        return [
            {
                'id': university.id,
                'title': university.title,
                'image': f'http://testserver/media/{university.image}',
                'type': university.type,
                'address': university.address,
                'founding_year': int(university.founding_year),
                'website': university.website
            }
            for university in self.universities
        ]

    def test_university_info(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.expected_data())
        self.assertEqual(len(response.data), 3)


class RecruitmentAnnouncementFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = RecruitmentAnnouncement

    title = factory.Faker('sentence', nb_words=2)
    description = factory.Faker('text', max_nb_chars=10)
    video = factory.Faker('url')
    created_at = factory.LazyFunction(timezone.now)


class RecruitmentAnnouncementFileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = RecruitmentAnnouncementFile

    title = factory.Faker('sentence', nb_words=2)
    link = factory.django.FileField(filename='test_file.pdf')
    recruitment_announcement = factory.SubFactory(RecruitmentAnnouncementFactory)


class RecruitmentAnnouncementTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.announcements = RecruitmentAnnouncementFactory.create_batch(3)

        for announcement in self.announcements:
            RecruitmentAnnouncementFileFactory.create_batch(2, recruitment_announcement=announcement)

    def expected_list_data(self):
        return [
            {
                'id': announcement.id,
                'title': announcement.title,
                'created_at': announcement.created_at.strftime('%d.%m.%Y'),
            }
            for announcement in self.announcements
        ]

    def expected_detail_data(self, announcement):
        return {
            'id': announcement.id,
            'title': announcement.title,
            'description': announcement.description,
            'video': announcement.video,
            'created_at': announcement.created_at.strftime('%d.%m.%Y'),
            'recruitment_file': [
                {
                    'id': file.id,
                    'title': file.title,
                    'link': f'http://testserver/media/{file.link}'
                }
                for file in announcement.recruitment_file.all()
            ]
        }

    def test_recruitment_announcement_list(self):
        response = self.client.get(reverse('recruitment'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data = response.data
        expected_data = self.expected_list_data()

        self.assertEqual(len(response_data), len(expected_data))

        for item in expected_data:
            self.assertIn(item, response_data)

    def test_recruitment_announcement_detail(self):
        announcement = self.announcements[0]
        response = self.client.get(reverse('recruitment_detail', kwargs={'pk': announcement.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_data = self.expected_detail_data(announcement)

        self.assertEqual(response.data, expected_data)
