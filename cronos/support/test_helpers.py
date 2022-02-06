import base64
from django.contrib.auth.models import User
from rest_framework import HTTP_HEADER_ENCODING
from cronos.models import File
from rest_framework.test import APIRequestFactory


def get_basic_credentials(username: str, password: str):
    User.objects.create_user(username=username, password=password)

    credentials = f"{username}:{password}"
    base64_credentials = base64.b64encode(
        credentials.encode(HTTP_HEADER_ENCODING)
    ).decode(HTTP_HEADER_ENCODING)

    return base64_credentials
