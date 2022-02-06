from django.urls import reverse
from cronos.support.test_helpers import get_basic_credentials
from rest_framework import status
from rest_framework.test import APITestCase


class FileAPITestCase(APITestCase):
    def setUp(self):
        self.url_list = reverse("cronos:files-list")
        self.credentials = get_basic_credentials(username="sergio", password="test")

        with open("cronos/domains/files/test/Sergio Ramos.png", "rb") as file:
            response = self.client.post(
                path=self.url_list,
                data={"path": file},
                HTTP_AUTHORIZATION=f"Basic {self.credentials}",
            )

            self.test_file_uuid = response.json().get("uuid")

    def test_create_file(self):
        with open("cronos/domains/files/test/Sergio Ramos.png", "rb") as file:
            response = self.client.post(
                path=self.url_list,
                data={"path": file},
                HTTP_AUTHORIZATION=f"Basic {self.credentials}",
            )

            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_files(self):
        response = self.client.get(path=self.url_list)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_file(self):
        response = self.client.get(
            path=reverse("cronos:files-detail", args=[self.test_file_uuid]), HTTP_AUTHORIZATION=f"Basic {self.credentials}"
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_file(self):
        with open("cronos/domains/files/test/test-image.jpg", "rb") as file:
            response = self.client.put(
                path=reverse("cronos:files-detail", args=[self.test_file_uuid]),
                data={"path": file},
                HTTP_AUTHORIZATION=f"Basic {self.credentials}"
            )
            
            self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_destroy_file(self):
        response = self.client.delete(
            path=reverse("cronos:files-detail", args=[self.test_file_uuid]),
            HTTP_AUTHORIZATION=f"Basic {self.credentials}"
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)