from django.http import Http404
from rest_framework.generics import RetrieveAPIView


class LatestObjectRetrieveAPIView(RetrieveAPIView):
    model = None
    serializer_class = None
    lookup_field = 'id'

    def get_object(self):
        try:
            return self.model.objects.latest('id')
        except self.model.DoesNotExist:
            raise Http404(f"No {self.model.__name__} objects found")
