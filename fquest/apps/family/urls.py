#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: The URL mapping for the 'family' application.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.conf.urls import patterns, url
from views import *


urlpatterns = patterns('fquest.apps.family',

        url(r'^tree/(?P<family_id>\d)/chart/$', 'views.tree_chart',
            {'restricted': False}, name='tree_chart_complete'),

        url(r'^tree/(?P<family_id>\d)/chart/restricted/$', 'views.tree_chart',
            {'restricted': True}, name='tree_chart_restricted'),
)


# vim:ft=python ts=4 tw=80 cc=+1:
