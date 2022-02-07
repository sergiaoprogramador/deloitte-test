import base64
import random
import string
from cronos.models import File, Member, Post, Service
from django.contrib.auth.models import User
from rest_framework import HTTP_HEADER_ENCODING


def get_basic_credentials(username: str, password: str):
    User.objects.create_user(username=username, password=password)

    credentials = f"{username}:{password}"
    base64_credentials = base64.b64encode(
        credentials.encode(HTTP_HEADER_ENCODING)
    ).decode(HTTP_HEADER_ENCODING)

    return base64_credentials


def random_char(length: int = 5):
    return "".join(random.choice(string.ascii_letters) for n in range(length))


def create_generic_member(
    first_name: str,
    last_name: str,
    email: str = None,
    linkedin: str = f"{random_char()}",
    position: str = f"{random_char()}",
    about: str = f"{random_char()}",
    profile_picture: File = None,
) -> Member:
    email = email if email else f"{random_char()}@gmail.com"
    return Member.objects.create(
        first_name=first_name,
        last_name=last_name,
        email=email,
        linkedin=linkedin,
        position=position,
        about=about,
        profile_picture=profile_picture,
    )


def create_generic_member_object(
    first_name: str,
    last_name: str,
    email: str = None,
    linkedin: str = f"{random_char()}",
    position: str = f"{random_char()}",
    about: str = f"{random_char()}",
    profile_picture: str = None,
) -> dict:
    email = email if email else f"{random_char()}@gmail.com"
    return {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "linkedin": linkedin,
        "position": position,
        "about": about,
        "profile_picture": profile_picture,
    }


def create_generic_post(
    title: str,
    content: str = f"{random_char()}",
    cover_image: File = None,
) -> Post:
    return Post.objects.create(
        title=title,
        content=content,
        cover_image=cover_image,
    )


def create_generic_post_object(
    title: str,
    content: str = f"{random_char()}",
    cover_image: str = None,
) -> dict:
    return {
        "title": title,
        "content": content,
        "cover_image": cover_image,
    }


def create_generic_service(
    title: str,
    description: str = f"{random_char()}",
    image: File = None,
) -> Service:
    return Service.objects.create(
        title=title,
        description=description,
        image=image,
    )


def create_generic_service_object(
    title: str,
    description: str = f"{random_char()}",
    image: str = None,
) -> dict:
    return {
        "title": title,
        "description": description,
        "image": image,
    }
