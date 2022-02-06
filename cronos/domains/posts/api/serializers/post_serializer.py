from cronos.models import Post, File
from cronos.serializers import FileSerializer
from rest_framework import serializers


class CoverImage(serializers.RelatedField):
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


class PostSerializer(serializers.ModelSerializer):
    cover_image = CoverImage(required=False)

    class Meta:
        model = Post
        fields = ["title", "content", "cover_image", "uuid"]

    def is_valid(self, **kwargs):
        if "cover_image" in self.initial_data:
            self.initial_data["cover_image"] = File.objects.get(
                uuid=self.initial_data["cover_image"]
            )

        return super(PostSerializer, self).is_valid()
