from cronos.models import Member
from cronos.serializers import MemberSerializer
from rest_framework import viewsets, permissions


class MemberViewSet(viewsets.ModelViewSet):
    def get_object(self):
        return self.queryset.get(uuid=self.kwargs.get("pk"))

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
