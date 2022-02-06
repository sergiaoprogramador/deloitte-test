from rest_framework import serializers
from cronos.models import File


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ["path", "uuid"]
