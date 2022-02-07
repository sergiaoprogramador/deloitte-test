from django.urls import reverse
from cronos.support.test_helpers import (
    get_basic_credentials,
    create_generic_post,
    create_generic_post_object,
)
from rest_framework import status
from rest_framework.test import APITestCase


class PostAPITestCase(APITestCase):
    def setUp(self):
        self.url_list = reverse("cronos:posts-list")
        self.credentials = get_basic_credentials(username="sergio", password="test")
        self.test_post = create_generic_post(
            title="New Post Test", content="Test content"
        )

        with open("cronos/domains/files/test/Sergio Ramos.png", "rb") as file:
            response = self.client.post(
                path=reverse("cronos:files-list"),
                data={"path": file},
                HTTP_AUTHORIZATION=f"Basic {self.credentials}",
            )

            self.test_file_uuid = response.json().get("uuid")

    def test_create_post(self):
        post_payload = create_generic_post_object(
            title="Test Post", content="Test Content", cover_image=self.test_file_uuid
        )

        response = self.client.post(
            path=self.url_list,
            data=post_payload,
            format="json",
            HTTP_AUTHORIZATION=f"Basic {self.credentials}",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_posts(self):
        response = self.client.get(path=self.url_list)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_post(self):
        response = self.client.get(
            path=reverse("cronos:posts-detail", args=[self.test_post.uuid]),
            HTTP_AUTHORIZATION=f"Basic {self.credentials}",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update_post(self):
        post_payload = create_generic_post_object(
            title="Test post 2",
            content="Test content 2",
            cover_image=self.test_file_uuid,
        )

        response = self.client.patch(
            path=reverse("cronos:posts-detail", args=[self.test_post.uuid]),
            data=post_payload,
            format="json",
            HTTP_AUTHORIZATION=f"Basic {self.credentials}",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_destroy_post(self):
        response = self.client.delete(
            path=reverse("cronos:posts-detail", args=[self.test_post.uuid]),
            HTTP_AUTHORIZATION=f"Basic {self.credentials}",
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
