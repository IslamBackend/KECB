from django.http import Http404
from rest_framework.exceptions import NotFound
from rest_framework.generics import RetrieveAPIView

from apps.home.models import Banner
from apps.home.serializers import BannerSerializer


class LatestObjectRetrieveAPIView(RetrieveAPIView):
    model = None
    serializer_class = None
    lookup_field = 'id'
    type = None

    def get_object(self):
        if self.type is None:
            return self.model.objects.latest('id')

        try:
            return self.model.objects.filter(type=self.type).latest('id')
        except self.model.DoesNotExist:
            raise Http404(f"No {self.model.__name__} objects found")


class LatestBannerRetrieveAPIView(RetrieveAPIView):
    serializer_class = BannerSerializer
    page = None

    def get_object(self):
        obj = Banner.objects.filter(page=self.page).first()
        if obj is None:
            raise NotFound(f"Banner not found for page {self.page}")
        return obj
