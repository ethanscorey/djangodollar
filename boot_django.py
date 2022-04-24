"""This module sets up and configures Django.

Used by scripts that need to execute as if running in a Django server.

Original source: https://realpython.com/installable-django-app/
"""
import os
import django
from django.conf import settings

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "djangodollar"))

def boot_django():
    settings.configure(
        BASE_DIR=BASE_DIR,
        DEBUG=True,
        DATABASES={
            "default":{
                "ENGINE":"django.db.backends.sqlite3",
                "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
            }
        },
        INSTALLED_APPS=(
            "djangodollar",
        ),
        TIME_ZONE="UTC",
        USE_TZ=True,
    )
    django.setup()
