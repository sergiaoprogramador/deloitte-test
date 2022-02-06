from cronos.models import File, Member
from cronos.serializers import FileSerializer
from rest_framework import serializers


class ProfilePicture(serializers.RelatedField):
    def get_queryset(self):
        File.objects.all()

    def to_representation(self, value):
        serializer = FileSerializer(value)
        return {
            "uuid": str(serializer.data.get("uuid")),
            "path": serializer.data.get("path"),
        }

    def to_internal_value(self, data):
        return data


class MemberSerializer(serializers.ModelSerializer):
    profile_picture = ProfilePicture(required=False)

    class Meta:
        model = Member
        fields = [
            "first_name",
            "last_name",
            "profile_picture",
            "email",
            "position",
            "linkedin",
            "about",
            "uuid",
        ]

    def is_valid(self, **kwargs):
        if "profile_picture" in self.initial_data:
            self.initial_data["profile_picture"] = File.objects.get(
                uuid=self.initial_data["profile_picture"]
            )

        return super(MemberSerializer, self).is_valid()
