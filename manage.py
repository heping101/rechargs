#!/usr/bin/env python

import os
import sys
from site import addsitedir

D_APP_ROOT = os.path.abspath(os.path.dirname(__file__))

sys.path.insert(1, os.path.join(D_APP_ROOT, "apps"))
sys.path.insert(1, os.path.join(D_APP_ROOT, "vendor/apps"))

vendor_libs = addsitedir(os.path.join(D_APP_ROOT, "vendor/libs"), set())
if vendor_libs:
    sys.path = sys.path + list(vendor_libs)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "recharge.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
