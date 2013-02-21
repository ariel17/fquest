#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: The URL mapping for the 'timeline' application.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.conf.urls import patterns, url
from views import *


urlpatterns = patterns('fquest.apps.timeline',
        url(r'^events/$', 'views.events', name='events'),
)

# vim:ft=python ts=4 tw=80 cc=+1:
