from cronos.models import Post
from cronos.serializers import PostSerializer
from rest_framework import viewsets, permissions


class PostViewSet(viewsets.ModelViewSet):
    def get_object(self):
        return self.queryset.get(uuid=self.kwargs.get("pk"))

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
