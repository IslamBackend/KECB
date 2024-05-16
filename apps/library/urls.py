from django.urls import path

from apps.library.views import GalleryListView, GalleryDetailAPIView, EducationalMaterialListAPIView

urlpatterns = [
    path('library/gallery/', GalleryListView.as_view(), name='gallery_list'),
    path('library/gallery/<int:pk>/', GalleryDetailAPIView.as_view(), name='gallery_detail'),
    path('library/edu-materials/', EducationalMaterialListAPIView.as_view(), name='edu_material'),
]
