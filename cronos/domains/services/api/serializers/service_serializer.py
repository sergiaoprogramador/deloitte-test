from cronos.models import Service, File
from cronos.serializers import FileSerializer
from rest_framework import serializers


class Image(serializers.RelatedField):
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


class ServiceSerializer(serializers.ModelSerializer):
    image = Image(required=False)

    class Meta:
        model = Service
        fields = ["title", "description", "image", "uuid"]

    def is_valid(self, **kwargs):
        if "image" in self.initial_data:
            self.initial_data["image"] = File.objects.get(
                uuid=self.initial_data["image"]
            )

        return super(ServiceSerializer, self).is_valid()
