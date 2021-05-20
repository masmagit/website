import pytest
from django.urls import reverse
from django.conf import settings
from django.core import mail
# pytest main/tests/test-views.py

def test_settings_loaded():
    a = settings.ROOT_URLCONF
    assert a == "website.urls"

def test_view_contact_get(client):
    url = reverse("main:contact")
    response = client.get(url)
    assert response.status_code == 200

def test_view_contact_post(client):
    data = {
        'name' : 'Test name',
    	'email' : 'from@example.com',
        'subject' : 'test email',
        'message' : 'Hello test'
    }
    url = reverse("main:contact")
    response = client.post(url, data)
    assert response.status_code == 302
    assert len(mail.outbox) == 1
    assert mail.outbox[0].body.find('Email: from@example.com') > 0