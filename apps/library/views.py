from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from apps.library.models import Gallery, EducationalMaterial
from apps.library.serializers import GallerySerializer, GalleryDetailSerializer, EducationalMaterialSerializer


class GalleryListView(APIView):
    def get(self, request):
        queryset = Gallery.objects.all()
        serializer = GallerySerializer(queryset, context={"request": request}, many=True)
        return Response(serializer.data)


class GalleryDetailAPIView(RetrieveAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GalleryDetailSerializer


class EducationalMaterialListAPIView(ListAPIView):
    queryset = EducationalMaterial.objects.all()
    serializer_class = EducationalMaterialSerializer
