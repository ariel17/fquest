#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: The URL mapping for the 'family' application.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy
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

        # Family URL

        url(r'^family/$', list_detail.object_list, family_info,
            name='family_list'),

        url(r'^family/(?P<object_id>\d+)/$', family_detail,
            name='family_detail'),

        url(r'^family/add/$', create_update.create_object, {'model': Family,
            'template_name': 'form.html', 'extra_context': {'model': Family},
            'post_save_redirect': reverse_lazy('family_list')},
            name='family_add'),

        url(r'^family/edit/(?P<object_id>\d+)/$', create_update.update_object,
            {'model': Family, 'template_name': 'form.html',
                'extra_context': {'model': Family},
                'post_save_redirect': reverse_lazy('family_list')},
            name='family_edit'),

        # Person URL

        url(r'^person/$', list_detail.object_list, person_info,
            name='person_list'),

        url(r'^person/(?P<object_id>\d+)/$', list_detail.object_detail,
            person_info, name='person_detail'),

        url(r'^person/add/$', create_update.create_object, {'model': Person,
            'template_name': 'form.html',
            'post_save_redirect': reverse_lazy('person_list')},
            name='person_add'),

        url(r'^person/edit/(?P<object_id>\d+)/$', create_update.update_object,
            {'model': Person, 'template_name': 'form.html',
                'extra_context': {'model': Person},
                'post_save_redirect': reverse_lazy('person_list')},
            name='person_edit'),

        # Tree URL

        url(r'^tree/(?P<family_id>\d+)/chart/$', tree_chart,
            {'restricted': False}, name='tree_chart_complete'),

        url(r'^tree/(?P<family_id>\d+)/chart/restricted/$', tree_chart,
            {'restricted': True}, name='tree_chart_restricted'),
)

# vim:ft=python ts=4 tw=80 cc=+1:
