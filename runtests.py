#!/usr/bin/env python
import os
import sys

#DIRNAME = os.path.join(os.path.dirname(__file__))

#sys.path.append(DIRNAME)
#sys.path.append(os.path.join(DIRNAME, 'src'))


import django
from django.conf import settings
from django.test.utils import get_runner

if __name__ == "__main__":
    os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.test_settings'
    django.setup()
    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests(["tests"])
    sys.exit(bool(failures))
