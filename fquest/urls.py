#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Exposes the URI mapping through project applications.
"""
__author__ = "Ariel Gerardo Ríos (ariel.gerardo.rios@gmail.com)"


from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fquest.views.home', name='home'),
    url(r'^fquest/family/', include('fquest.apps.family.urls')),
    url(r'^fquest/timeline/', include('fquest.apps.timeline.urls')),

    # Language selection
    url(r'^i18n/', include('django.conf.urls.i18n')),

    # Accout creation
    url(r'^accounts/', include('registration.backends.default.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
            url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                'document_root': settings.MEDIA_ROOT,
            }),
        )


# vim:ft=python ts=4 tw=80 cc=+1:
