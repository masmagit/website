import sys, os, dj_database_url, dotenv

# Load environment vars here for pytest
dotenv.load_dotenv(os.path.join(os.path.abspath(os.path.dirname(__name__)), '.env'))

from website.settings.base import *

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

if (len(sys.argv) > 0) and (sys.argv[1] != 'collectstatic'):
    if os.getenv("DATABASE_URL", None) is None:
        raise Exception("DATABASE_URL environment variable not defined")
    DATABASES = {
        "default": dj_database_url.parse(os.environ.get("DATABASE_URL")),
    }