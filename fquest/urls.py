#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Exposes the URI mapping through project applications.
"""
__author__ = "Ariel Gerardo Ríos (ariel.gerardo.rios@gmail.com)"


from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fquest.views.home', name='home'),
    url(r'^fquest/family/', include('fquest.apps.family.urls')),
    url(r'^fquest/timeline/', include('fquest.apps.timeline.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

# vim:ft=python ts=4 tw=80 cc=+1:
