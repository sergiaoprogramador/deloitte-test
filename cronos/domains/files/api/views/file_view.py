from cronos.models import File
from cronos.serializers import FileSerializer
from rest_framework import viewsets, permissions


class FileViewSet(viewsets.ModelViewSet):
    def get_object(self):
        return self.queryset.get(uuid=self.kwargs.get("pk"))

    permission_classes = [permissions.IsAuthenticated]
    queryset = File.objects.all()
    serializer_class = FileSerializer
