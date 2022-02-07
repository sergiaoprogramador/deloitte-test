from django.urls import reverse
from cronos.support.test_helpers import (
    get_basic_credentials,
    create_generic_service,
    create_generic_service_object,
)
from rest_framework import status
from rest_framework.test import APITestCase


class ServiceAPITestCase(APITestCase):
    def setUp(self):
        self.url_list = reverse("cronos:services-list")
        self.credentials = get_basic_credentials(username="sergio", password="test")
        self.test_service = create_generic_service(
            title="New Service Test", description="Test description"
        )

        with open("cronos/domains/files/test/Sergio Ramos.png", "rb") as file:
            response = self.client.post(
                path=reverse("cronos:files-list"),
                data={"path": file},
                HTTP_AUTHORIZATION=f"Basic {self.credentials}",
            )

            self.test_file_uuid = response.json().get("uuid")

    def test_create_service(self):
        service_payload = create_generic_service_object(
            title="Test Service", description="Test description", image=self.test_file_uuid
        )

        response = self.client.post(
            path=self.url_list,
            data=service_payload,
            format="json",
            HTTP_AUTHORIZATION=f"Basic {self.credentials}",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_services(self):
        response = self.client.get(path=self.url_list)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_service(self):
        response = self.client.get(
            path=reverse("cronos:services-detail", args=[self.test_service.uuid]),
            HTTP_AUTHORIZATION=f"Basic {self.credentials}",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update_service(self):
        service_payload = create_generic_service_object(
            title="Test post 2",
            description="Test content 2",
            image=self.test_file_uuid,
        )

        response = self.client.patch(
            path=reverse("cronos:services-detail", args=[self.test_service.uuid]),
            data=service_payload,
            format="json",
            HTTP_AUTHORIZATION=f"Basic {self.credentials}",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_destroy_service(self):
        response = self.client.delete(
            path=reverse("cronos:services-detail", args=[self.test_service.uuid]),
            HTTP_AUTHORIZATION=f"Basic {self.credentials}",
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
