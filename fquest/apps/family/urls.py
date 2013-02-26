#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: The URL mapping for the 'family' application.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.conf.urls import patterns, url
from django.views.generic.list_detail import object_detail
from models import Person
from views import tree_chart


person_info = {
    'queryset': Person.objects.all(),
}

urlpatterns = patterns('fquest.apps.family',

        url(r'^person/(?P<object_id>\d+)/$', object_detail, person_info,
            name='person_show'),

        url(r'^tree/(?P<family_id>\d+)/chart/$', tree_chart,
            {'restricted': False}, name='tree_chart_complete'),

        url(r'^tree/(?P<family_id>\d+)/chart/restricted/$', tree_chart,
            {'restricted': True}, name='tree_chart_restricted'),
)


# vim:ft=python ts=4 tw=80 cc=+1:
