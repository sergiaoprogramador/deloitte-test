from cronos.models import Service
from cronos.serializers import ServiceSerializer
from rest_framework import viewsets, permissions


class ServiceViewSet(viewsets.ModelViewSet):
    def get_object(self):
        return self.queryset.get(uuid=self.kwargs.get("pk"))

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Service.objects.all().order_by("created")
    serializer_class = ServiceSerializer
