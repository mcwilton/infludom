import json
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse, reverse_lazy
from django.utils.functional import lazy

from .views import TalentViews
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.test import APITestCase
from .serializer import TalentSerializer
import pytest

from .models import Talent
#
class ViewTestCase(APITestCase):
    def test_view_case(self):
        data = {"username": "testman", "password1": "testpassword", "password2": "testpassword"}
        response   = self.client.post("api-auth", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class RegistrationCase(APITestCase):
    def test_registration_case(self):
        data = {"username": "testman", "password1": "testpassword", "password2": "testpassword"}
        response   = self.client.post("api-auth", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        

#
# class ProfileViewSetTestCase(APITestCase):
#
#     list_url = reverse("profile-list")
#
#     def setUp(self):
#         self.user = User.objects.create_user(username="davinci",
#                                              password="some-very-strong-psw")
#         self.token = Token.objects.create(user=self.user)
#         self.api_authentication()
#
#     def api_authentication(self):
#         self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
#
#     def test_profile_list_authenticated(self):
#         response = self.client.get(self.list_url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_profile_list_un_authenticated(self):
#         self.client.force_authenticate(user=None)
#         response = self.client.get(self.list_url)
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
#
#     def test_profile_detail_retrieve(self):
#         response = self.client.get(reverse("profile-detail", kwargs={"pk": 1}))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data["user"], "davinci")
#
#     def test_profile_update_by_owner(self):
#         response = self.client.put(reverse("profile-detail", kwargs={"pk": 1}),
#                                    {"city": "Anchiano", "bio": "Renaissance Genius"})
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(json.loads(response.content),
#                          {"id": 1, "user": "davinci", "bio": "Renaissance Genius",
#                           "city": "Anchiano", "avatar": None})
#
#     def test_profile_update_by_random_user(self):
#         random_user = User.objects.create_user(username="random",
#                                                password="psw123123123")
#         self.client.force_authenticate(user=random_user)
#         response = self.client.put(reverse("profile-detail", kwargs={"pk": 1}),
#                                    {"bio": "hacked!!!"})
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

