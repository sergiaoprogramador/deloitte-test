from cronos.models import File
from cronos.serializers import FileSerializer
from rest_framework import generics


class FileList(generics.ListCreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer


class FileDetail(generics.RetrieveUpdateDestroyAPIView):
    def get_object(self):
        return self.queryset.get(uuid=self.kwargs.get("pk"))

    queryset = File.objects.all()
    serializer_class = FileSerializer
