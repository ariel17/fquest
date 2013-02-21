#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Administration classes for 'timeline' application models.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.contrib import admin
from django.utils.translation import ugettext as _
from fquest.libs.admin.utils import persons2admin
from models import Event, Type


class EventAdmin(admin.ModelAdmin):
    """
    Administration class for model class Event.
    """
    list_display = ['id', 'occurred_in', 'type', 'persons_admin',
            'description']

    def persons_admin(self, obj):
        """
        Returns an HTML string with links to the Person objects related to the
        current event.
        """
        return persons2admin(obj.persons.all())

    persons_admin.allow_tags = True
    persons_admin.short_description = _('Persons involved')


admin.site.register(Event, EventAdmin)


class TypeAdmin(admin.ModelAdmin):
    """
    Administration class for model class Type.
    """
    list_display = ['id', 'name', 'description']


admin.site.register(Type, TypeAdmin)

# vim:ft=python ts=4 tw=80 cc=+1:
