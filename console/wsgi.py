"""
WSGI config for recharge project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

# pylint: disable = invalid-name

import os
import sys
from site import addsitedir

D_APP_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

sys.path.insert(1, os.path.join(D_APP_ROOT, "apps"))
sys.path.insert(1, os.path.join(D_APP_ROOT, "vendor/apps"))

vendor_libs = addsitedir(os.path.join(D_APP_ROOT, "vendor/libs"), set())
if vendor_libs:
    sys.path = sys.path + list(vendor_libs)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "console.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()