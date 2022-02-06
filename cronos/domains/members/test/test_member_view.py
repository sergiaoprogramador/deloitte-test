from django.urls import reverse
from cronos.support.test_helpers import (
    get_basic_credentials,
    create_generic_member,
    create_generic_member_object,
)
from rest_framework import status
from rest_framework.test import APITestCase


class MemberAPITestCase(APITestCase):
    def setUp(self):
        self.url_list = reverse("cronos:members-list")
        self.credentials = get_basic_credentials(username="sergio", password="test")
        self.test_member = create_generic_member(first_name="Sergio", last_name="Ramos")

        with open("cronos/domains/files/test/Sergio Ramos.png", "rb") as file:
            response = self.client.post(
                path=self.url_list,
                data={"path": file},
                HTTP_AUTHORIZATION=f"Basic {self.credentials}",
            )

            self.test_file_uuid = response.json().get("uuid")

    def test_create_member(self):
        member_payload = create_generic_member_object(
            first_name="Jose", last_name="Rocha"
        )

        response = self.client.post(
            path=self.url_list,
            data=member_payload,
            format="json",
            HTTP_AUTHORIZATION=f"Basic {self.credentials}",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_members(self):
        response = self.client.get(path=self.url_list)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_member(self):
        response = self.client.get(
            path=reverse("cronos:members-detail", args=[self.test_member.uuid]),
            HTTP_AUTHORIZATION=f"Basic {self.credentials}",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update_member(self):
        member_payload = create_generic_member_object(
            first_name="Alterar", last_name="Nome", position="Software Engineer"
        )

        response = self.client.patch(
            path=reverse("cronos:members-detail", args=[self.test_member.uuid]),
            HTTP_AUTHORIZATION=f"Basic {self.credentials}",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_destroy_member(self):
        response = self.client.delete(
            path=reverse("cronos:members-detail", args=[self.test_member.uuid]),
            HTTP_AUTHORIZATION=f"Basic {self.credentials}",
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
