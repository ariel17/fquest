#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Description: Django settings for development stage.
"""
__author__ = "Ariel Gerardo Ríos (ariel.gerardo.rios@gmail.com)"


import os
import common

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = 'http://localhost:8000/media/'

MIDDLEWARE_CLASSES += (
    # Debug toolbar
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INSTALLED_APPS += (
    # Debug toolbar
    'debug_toolbar',
)
