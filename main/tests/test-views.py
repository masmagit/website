import pytest
from django.urls import reverse
from django.conf import settings
# pytest main/tests/test-views.py

def test_settings_loaded():
    a = settings.ROOT_URLCONF
    assert a == "website.urls"

#https://docs.djangoproject.com/en/dev/topics/testing/tools/#topics-testing-email
def test_view_contact_get(client):
    url = reverse("main:contact")
    response = client.get(url)
    assert response.status_code == 200

def test_view_contact_post(client):
    pass