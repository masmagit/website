import pytest

@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart(session):
    pass

# Set environment variables for the tests
@pytest.fixture(autouse=True)
def env_setup(monkeypatch):
    monkeypatch.setenv('EMAIL_BACKEND', 'django.core.mail.backends.locmem.EmailBackend')
    # use reCaptcha open testing keys
    monkeypatch.setenv('RECAPTCHA_SITE_KEY', '6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI')
    monkeypatch.setenv('RECAPTCHA_SECRET_KEY', '6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe')