import factory
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from apps.announcement.models import Announcement
from apps.center_info.tests import RubricFactory
from apps.home.constants import PAGE_CHOICES
from apps.home.models import Banner, SocialInfo, KoreanSite
from apps.library.models import Gallery
from apps.library.tests import GalleryFactory


class BannerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Banner

    title = factory.Faker('word')
    description = factory.Faker('sentence', nb_words=3)
    image = factory.django.ImageField(filename='test_image.jpg')
    page = factory.Iterator([choice[0] for choice in PAGE_CHOICES])


class BannerTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.banner = BannerFactory.create(page='Главная')

    def expected_date(self):
        return {
            'id': self.banner.id,
            'title': self.banner.title,
            'description': self.banner.description,
            'image': f'http://testserver/media/{self.banner.image}',
        }

    def test_banner(self):
        response = self.client.get(reverse('home_banner'))
        self.assertTrue(Banner.objects.exists())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.expected_date())


class SocialInfoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SocialInfo

    image = factory.django.ImageField(filename='test_image.jpg')
    phone_number_first = factory.Faker('phone_number')
    phone_number_second = factory.Faker('phone_number')
    email = factory.Faker('email')
    working_hours = factory.Faker('text', max_nb_chars=100)
    longitude = '300.000000'
    latitude = '300.000000'
    telegram_url = factory.Faker('url')
    whatsapp_url_first = factory.Faker('url')
    whatsapp_url_second = factory.Faker('url')
    instagram_url = factory.Faker('url')
    youtube_url = factory.Faker('url')
    facebook_url = factory.Faker('url')
    twitter_url = factory.Faker('url')


class SocialInfoTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.social_info = SocialInfoFactory()

    def expected_data(self):
        return {
            'id': self.social_info.id,
            'image': f'http://testserver/media/{self.social_info.image}',
            'phone_number_first': self.social_info.phone_number_first,
            'phone_number_second': self.social_info.phone_number_second,
            'email': self.social_info.email,
            'working_hours': self.social_info.working_hours,
            'longitude': self.social_info.longitude,
            'latitude': self.social_info.latitude,
            'telegram_url': self.social_info.telegram_url,
            'whatsapp_url_first': self.social_info.whatsapp_url_first,
            'whatsapp_url_second': self.social_info.whatsapp_url_second,
            'instagram_url': self.social_info.instagram_url,
            'youtube_url': self.social_info.youtube_url,
            'facebook_url': self.social_info.facebook_url,
            'twitter_url': self.social_info.twitter_url
        }

    def test_social_info(self):
        url = reverse('social_info')
        response = self.client.get(url)
        self.assertTrue(SocialInfo.objects.exists())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.expected_data())


class KoreanSiteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = KoreanSite

    logo = factory.django.ImageField(filename='test_logo.jpg')
    name = factory.Faker('company')
    url = factory.Faker('url')


class KoreanSiteTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.korean_site = KoreanSiteFactory.create_batch(3)

    def expected_data(self):
        return [
            {
                'id': site.id,
                'logo': f'http://testserver/media/{site.logo}',
                'name': site.name,
                'url': site.url
            }
            for site in self.korean_site
        ]

    def test_korean_site(self):
        response = self.client.get(reverse('korean_site'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

        for site_data in response.data:
            self.assertIn(site_data, self.expected_data())


class AnnouncementFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Announcement

    title = factory.Faker('sentence', nb_words=4)
    description = factory.Faker('paragraph')
    rubric = factory.SubFactory(RubricFactory)
    image = factory.django.ImageField(filename='test_image.jpg')


class SearchListAPITest(APITestCase):
    def setUp(self):
        self.gallery1 = GalleryFactory(title="Nature Gallery", description="Beautiful nature pictures")
        self.gallery2 = GalleryFactory(title="Urban Gallery", description="City landscapes")
        self.announcement1 = AnnouncementFactory(title="Nature Announcement",
                                                 description="Announcement about nature event")
        self.announcement2 = AnnouncementFactory(title="Urban Announcement",
                                                 description="Announcement about urban event")
        self.url = reverse('search')

    def test_search_results_nature(self):
        response = self.client.get(self.url, {'q': 'Nature'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.data

        self.assertEqual(len(results['announcements']), 1)
        self.assertEqual(len(results['galleries']), 1)
        self.assertEqual(results['announcements'][0]['title'], self.announcement1.title)
        self.assertEqual(results['galleries'][0]['title'], self.gallery1.title)

    def test_search_results_urban(self):
        response = self.client.get(self.url, {'q': 'Urban'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.data

        self.assertEqual(len(results['announcements']), 1)
        self.assertEqual(len(results['galleries']), 1)
        self.assertEqual(results['announcements'][0]['title'], self.announcement2.title)
        self.assertEqual(results['galleries'][0]['title'], self.gallery2.title)

    def test_search_results_no_results(self):
        response = self.client.get(self.url, {'q': 'Nonexistent'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.data

        self.assertEqual(len(results['announcements']), 0)
        self.assertEqual(len(results['galleries']), 0)
