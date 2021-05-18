import pytest

@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart(session):
    pass

# Set environment variables for the tests
@pytest.fixture(autouse=True)
def env_setup(monkeypatch):
    monkeypatch.setenv('EMAIL_BACKEND', 'django.core.mail.backends.locmem.EmailBackend')