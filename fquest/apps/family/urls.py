#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: The URL mapping for the 'family' application.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.conf.urls import patterns, url
from django.views.generic import create_update
from django.views.generic import list_detail
from models import Family, Person
from views import tree_chart, family_detail


person_info = {
    'queryset': Person.objects.all(),
}

family_info = {
    'queryset': Family.objects.all(),
}

urlpatterns = patterns('fquest.apps.family',

        url(r'^family/add/$', create_update.create_object, {'model': Family},
            name='family_add'),

        url(r'^family/$', list_detail.object_list, family_info,
            name='family_list'),

        url(r'^family/(?P<object_id>\d+)/$', family_detail,
            name='family_detail'),

        url(r'^person/$', list_detail.object_list, person_info,
            name='person_list'),

        url(r'^person/(?P<object_id>\d+)/$', list_detail.object_detail,
            person_info, name='person_detail'),

        url(r'^tree/(?P<family_id>\d+)/chart/$', tree_chart,
            {'restricted': False}, name='tree_chart_complete'),

        url(r'^tree/(?P<family_id>\d+)/chart/restricted/$', tree_chart,
            {'restricted': True}, name='tree_chart_restricted'),
)


# vim:ft=python ts=4 tw=80 cc=+1:
