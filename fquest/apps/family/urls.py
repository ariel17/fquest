#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Description: The URL mapping for the 'family' application.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.conf.urls import patterns, url
from views import *


urlpatterns = patterns('fquest.apps.family',
        url(r'^tree/(?P<family_id>\d)/$', 'views.tree', name='family_tree'),
)
