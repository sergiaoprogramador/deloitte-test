from cronos.models import Service
from cronos.serializers import ServiceSerializer
from rest_framework import generics


class ServiceList(generics.ListCreateAPIView):
    queryset = Service.objects.all().order_by("created")
    serializer_class = ServiceSerializer


class ServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    def get_object(self):
        return self.queryset.get(uuid=self.kwargs.get("pk"))

    queryset = Service.objects.all().order_by("created")
    serializer_class = ServiceSerializer
