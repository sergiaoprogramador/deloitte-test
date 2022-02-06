from cronos.models import File
from cronos.serializers import FileSerializer
from rest_framework import viewsets, permissions
from rest_framework.parsers import FormParser, MultiPartParser


class FileViewSet(viewsets.ModelViewSet):
    def get_object(self):
        return self.queryset.get(uuid=self.kwargs.get("pk"))

    parser_classes = (FormParser, MultiPartParser)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = File.objects.all()
    serializer_class = FileSerializer
