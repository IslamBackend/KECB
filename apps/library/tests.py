import factory
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from apps.center_info.tests import RubricFactory
from apps.library.models import Gallery, GalleryImage, EducationalMaterial


class GalleryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Gallery

    title = factory.Faker('word')
    description = factory.Faker('text', max_nb_chars=100)
    created_at = factory.LazyFunction(timezone.now)
    rubric = factory.SubFactory(RubricFactory)


class GalleryImageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GalleryImage

    image = factory.django.ImageField(filename='test_image.jpg')
    gallery = factory.SubFactory(GalleryFactory)


class GalleryTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.gallery = GalleryFactory()
        self.gallery_image = GalleryImageFactory(gallery=self.gallery)

    def expected_data_list(self):
        image_url = f'http://testserver/media/{self.gallery_image.image.name}'
        return [
            {
                'id': self.gallery.id,
                'title': self.gallery.title,
                'first_image': image_url,
                'created_at': self.gallery.created_at.strftime('%d.%m.%Y'),
            }
        ]

    def expected_data_detail(self):
        image_url = f'http://testserver/media/{self.gallery_image.image.name}'
        return {
            'id': self.gallery.id,
            'title': self.gallery.title,
            'description': self.gallery.description,
            'created_at': self.gallery.created_at.strftime('%d.%m.%Y'),
            'gallery_images': [
                {
                    'id': self.gallery_image.id,
                    'image': image_url
                }
            ]
        }

    def test_gallery_list(self):
        response = self.client.get(reverse('gallery_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data = response.data
        expected_data_list = self.expected_data_list()

        self.assertGreater(len(response_data), 0)

        for item in response_data:
            self.assertIn(item, expected_data_list)

    def test_gallery_detail(self):
        response = self.client.get(reverse('gallery_detail', kwargs={'pk': self.gallery.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_data = self.expected_data_detail()

        self.assertEqual(response.data, expected_data)


class EducationalMaterialFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = EducationalMaterial

    title = factory.Faker('sentence', nb_words=4)
    link = factory.django.FileField(filename='test_material.pdf')


class EducationalMaterialTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.educational_material = EducationalMaterialFactory()

    def expected_data(self):
        file_url = f'http://testserver/media/{self.educational_material.link}'
        return {
            'id': self.educational_material.id,
            'title': self.educational_material.title,
            'link': file_url,
        }

    def test_educational_material(self):
        response = self.client.get(reverse('edu_material'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data = response.data
        expected_data = [self.expected_data()]

        self.assertEqual(len(response_data), 1)
        self.assertEqual(response_data, expected_data)
