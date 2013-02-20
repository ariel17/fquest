#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Description: The URL mapping for the 'person' application.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.conf.urls import patterns, url
from views import *


urlpatterns = patterns('fquest.apps.family',
        url(r'^tree/$', 'views.tree', name='tree'),
)
