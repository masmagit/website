import sys, dj_database_url, os
from website.settings.base import *

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

if not ((len(sys.argv) > 1) and (sys.argv[1] == 'collectstatic')):
    if os.getenv("DATABASE_URL", None) is None:
        raise Exception("DATABASE_URL environment variable not defined")
    DATABASES = {
        "default": dj_database_url.parse(os.environ.get("DATABASE_URL")),
    }