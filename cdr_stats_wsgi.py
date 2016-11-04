#!_env/bin/python

"""
WSGI script for usage in Virtalenvs with Apache - Embedded mod_wsgi

Heavily based on
http://blog.dscpl.com.au/2010/03/improved-wsgi-script-for-use-with.html
"""

import glob
import os.path
import sys

here = os.path.abspath(os.path.dirname(__file__))

sys.path.append(here)
sys.path.append(here + '/cdr_stats')

from cdr_stats import settings
import django.core.management

django.core.management.setup_environ(settings)
utility = django.core.management.ManagementUtility()
command = utility.fetch_command('runserver')

command.validate()

import django.conf
import django.utils

django.utils.translation.activate(django.conf.settings.LANGUAGE_CODE)

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
