import urllib
from json import loads as json_loads
from os import getenv as os_getenv

def recaptcha_validate(recaptcha_response):
    url = 'https://www.google.com/recaptcha/api/siteverify'
    values = {
        "secret": os_getenv("RECAPTCHA_SECRET_KEY"),
        "response": recaptcha_response
    }
    data = urllib.parse.urlencode(values).encode()
    request =  urllib.request.Request(url, data=data)
    response = urllib.request.urlopen(request)
    result = json_loads(response.read().decode())
    return result