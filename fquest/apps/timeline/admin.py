#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Description: Administration classes for 'timeline' application models.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.contrib import admin
from django.utils.translation import ugettext as _
from models import Event, Type


class EventAdmin(admin.ModelAdmin):
    """
    Administration class for model class Event.
    """
    list_display = ['id', 'occurred_in', 'type', 'description']


admin.site.register(Event, EventAdmin)


class TypeAdmin(admin.ModelAdmin):
    """
    Administration class for model class Type.
    """
    list_display = ['id', 'name', 'description']
    

admin.site.register(Type, TypeAdmin)
