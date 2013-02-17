#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Description: Admin class for 'person' applications' models.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.contrib import admin
from django.utils.translation import ugettext as _
from models import Person


class PersonAdmin(admin.ModelAdmin):
    """
    The administration class for model Person.
    """
    fieldsets = (
            (_('About his identification'), {
                'classes': ('extrapretty',),
                'fields': ('name', 'last_name')
            }),
            (_('About his lifetime dates'), {
                'classes': ('extrapretty',),
                'fields': ('born_in', 'deceased_in')
            }),
            (_('About his parents'), {
                'classes': ('extrapretty',),
                'fields': ('mother', 'father')
            }),
        )
    list_display = ['id', 'name', 'last_name', 'born_in', 'deceased_in']


admin.site.register(Person, PersonAdmin)
