#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Description: Person application class definitions.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.db import models
from django.utils.translation import ugettext as _


class Person(models.Model):
    """
    Represents the basic information about a person.
    """

    PARENT_HELP_TEXT = u'Select the person that will figure as parent, if it '\
            'exists in database.'

    NAME_FIELD_MAX_LENGH = 50

    name = models.CharField(_('Name'), max_length=NAME_FIELD_MAX_LENGH)
    last_name = models.CharField(_('Last Name'),
            max_length=NAME_FIELD_MAX_LENGH)
    born_in = models.DateTimeField(_('Born in'))
    deceased_in = models.DateTimeField(_('Deceased in'), blank=True, null=True)
    mother = models.ForeignKey('Person', related_name=_('Mother'), blank=True,
            null=True, help_text=_(PARENT_HELP_TEXT))
    father = models.ForeignKey('Person', related_name=_('Father'), blank=True,
            null=True, help_text=_(PARENT_HELP_TEXT))

    def __unicode__(self):
        return u"<Person id=%s name='%s' last_name='%s'>" % (repr(self.id),
                self.name, self.last_name)
