#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: The URL mapping for the 'family' application.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from models import Family, Person
from views import tree_chart


urlpatterns = patterns('fquest.apps.family',

        # Index

        url(r'^$', TemplateView.as_view(template_name='family_index.html'),
            name='family_index'),

        # Family URL

        url(r'^family/$', ListView.as_view(model=Family), name='family_list'),

        url(r'^family/(?P<pk>\d+)/$', DetailView.as_view(model=Family),
            name='family_detail'),

        url(r'^family/add/$', CreateView.as_view(model=Family,
            template_name='form.html', success_url=reverse_lazy('family_list')),
            name='family_add'),

        url(r'^family/edit/(?P<pk>\d+)/$', UpdateView.as_view(
            model=Family, template_name='form.html',
            success_url=reverse_lazy('family_list')), name='family_edit'),

        # Person URL

        url(r'^person/$', ListView.as_view(model=Person), name='person_list'),

        url(r'^person/(?P<pk>\d+)/$', DetailView.as_view(model=Person),
            name='person_detail'),

        url(r'^person/add/$', CreateView.as_view(model=Person,
            template_name='form.html', success_url=reverse_lazy('person_list')),
            name='person_add'),

        url(r'^person/edit/(?P<pk>\d+)/$', UpdateView.as_view(model=Person,
            template_name='form.html', success_url=reverse_lazy('person_list')),
            name='person_edit'),

        # Tree URL

        url(r'^tree/(?P<family_id>\d+)/chart/$', tree_chart,
            {'restricted': False}, name='tree_chart_complete'),

        url(r'^tree/(?P<family_id>\d+)/chart/restricted/$', tree_chart,
            {'restricted': True}, name='tree_chart_restricted'),
)

# vim:ft=python ts=4 tw=80 cc=+1:
