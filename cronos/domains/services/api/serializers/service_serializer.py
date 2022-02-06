from rest_framework import serializers
from cronos.models import Service


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ["description", "image", "title", "uuid"]
