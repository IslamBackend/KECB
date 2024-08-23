from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from apps.announcement.models import Announcement, Rubric, AnnouncementVideo, AnnouncementImage, AnnouncementFile


class AnnouncementTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.rubric = Rubric.objects.create(title="Тестовая рубрика")
        self.announcement = Announcement.objects.create(
            rubric=self.rubric,
            title="Тестовое объявление",
            image="image.jpg",
            description="Тестовое описание"
        )
        self.file = AnnouncementFile.objects.create(
            title="Тестовый файл",
            file_path="file.pdf",
            announcement=self.announcement
        )
        self.video = AnnouncementVideo.objects.create(
            link="http://example.com/video",
            announcement=self.announcement
        )
        self.image = AnnouncementImage.objects.create(
            image="image2.jpg",
            announcement=self.announcement
        )

        self.expected_list_data = {
            'id': self.announcement.id,
            'title': self.announcement.title,
            'image': f'http://testserver/media/{self.announcement.image}',
            'rubric': self.rubric.title,
            'created_at': self.announcement.created_at.strftime('%d.%m.%Y')
        }

        self.expected_detail_data = {
            'id': self.announcement.id,
            'title': self.announcement.title,
            'image': f'http://testserver/media/{self.announcement.image}',
            'rubric': self.rubric.title,
            'description': self.announcement.description,
            'images': [
                {
                    'id': self.image.id,
                    'image': f'http://testserver/media/{self.image.image}',
                }
            ],
            'videos': [
                {
                    'id': self.video.id,
                    'link': self.video.link,
                }
            ],
            'files': [
                {
                    'id': self.file.id,
                    'title': self.file.title,
                    'file_path': f'http://testserver/media/{self.file.file_path}',
                }
            ],
            'created_at': self.announcement.created_at.strftime('%d.%m.%Y')
        }

    def test_announcement_list(self):
        response = self.client.get(reverse('announcement_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertIn(self.expected_list_data, response.data['results'])

    def test_announcement_detail(self):
        response = self.client.get(reverse('announcement_detail', kwargs={'pk': self.announcement.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.expected_detail_data)
