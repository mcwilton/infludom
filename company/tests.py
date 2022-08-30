from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .serializer import ProjectSerializer
import pytest

from .models import Project

