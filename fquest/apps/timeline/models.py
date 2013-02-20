#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Description: Class models for application 'timeline'.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.db import models
from django.utils.translation import ugettext as _
from fquest.apps.family.models import Person


class Event(models.Model):
    """
    Describes an occurred event in the past.
    """
    occurred_in = models.DateTimeField(_('Occurred in'))
    type = models.ForeignKey('Type', related_name=_('Type'))
    persons = models.ManyToManyField(Person)
    description = models.TextField(_('What happened?'), help_text=_('Explain '
            'what happened in that event.'))

    def __unicode__(self):
        return u"<Event id=%s occured_in='%s' type=%s>" % (repr(self.id),
                self.occurred_in, self.type.name)


class Type(models.Model):
    """
    Defines an event type.
    """
    name = models.CharField(_('Name'), unique=True, max_length=50)
    description = models.CharField(_('Description'), max_length=100)

    def __unicode__(self):
        return u"%s" % self.name

# vim:ft=python ts=4 tw=80 cc=+1:
