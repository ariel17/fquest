#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: The URL mapping for the 'timeline' application.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.conf.urls import patterns, url
from views import *


urlpatterns = patterns('fquest.apps.timeline',

        url(r'^(?P<family_id>\d+)/$', 'views.events',
            {'template': 'timeline_base.html'}, name='events_format'),

        url(r'^(?P<family_id>\d+)/simple/$', 'views.events',
            {'template': 'events_simple.html'}, name='events_simple'),
)


# vim:ft=python ts=4 tw=80 cc=+1:
