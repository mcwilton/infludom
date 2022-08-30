from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .serializer import ProjectSerializer
import pytest

from .models import Project

@pytest.mark.django_db
def test_talent_list(client):
    url = reverse('ProjectsView')
    response = client.get(url)

    projects = Project.objects.all()
    expected_data = ProjectSerializer(projects, many=True).data

    assert response.status_code == 200
    assert response.data == expected_data