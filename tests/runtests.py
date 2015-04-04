#!/usr/bin/env python
import os
import sys

DIRNAME = os.path.join(os.path.dirname(__file__), '..')

sys.path.append(DIRNAME)
sys.path.append(os.path.join(DIRNAME, 'src'))

# must be defined before import of settings in Django < 1.7
os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.test_settings'

import django
from django.conf import settings
from django.test.utils import get_runner

if __name__ == "__main__":
    if django.VERSION[0] == 1 and django.VERSION[1] < 7:
        from django.test.utils import setup_test_environment
        setup_test_environment()

    if django.VERSION[0] == 1 and django.VERSION[1] >= 7:
        django.setup()

    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests(["geelweb.django.navhelper"])
    sys.exit(bool(failures))
