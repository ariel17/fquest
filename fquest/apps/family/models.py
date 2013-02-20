#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Description: 'family' application class definitions.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.db import models
from django.utils.translation import ugettext as _


NAME_FIELD_MAX_LENGH = 50


class Family(models.Model):
    """
    A family identification.
    """

    sure_name = models.CharField(_('Sure Name'),
            max_length=NAME_FIELD_MAX_LENGH)

    class Meta:
        verbose_name_plural = "Families"

    def __unicode__(self):
        return unicode(self.sure_name)
    

class Person(models.Model):
    """
    Represents the basic information about a person.
    """

    PARENT_HELP_TEXT = u'Select the person that will figure as parent, if it '\
            'exists in database.'

    SEX_MALE_CHOICE = 'M'

    SEX_FEMALE_CHOICE = 'F'

    SEX_CHOICES = (
            (SEX_MALE_CHOICE, _('Male')),
            (SEX_FEMALE_CHOICE, _('Female')),
            )

    name = models.CharField(_('Name'), max_length=NAME_FIELD_MAX_LENGH)
    family = models.ForeignKey('Family', related_name=_('Family'))
    sex = models.CharField(_('Sex'), max_length=2, choices=SEX_CHOICES)
    born_in = models.DateTimeField(_('Born in'))
    deceased_in = models.DateTimeField(_('Deceased in'), blank=True, null=True)
    mother = models.ForeignKey('Person', related_name=_('Mother'), blank=True,
            null=True, help_text=_(PARENT_HELP_TEXT))
    father = models.ForeignKey('Person', related_name=_('Father'), blank=True,
            null=True, help_text=_(PARENT_HELP_TEXT))

    def __unicode__(self):
        return u"%s %s (%s) - %s" % (self.name, self.family.sure_name, self.sex,
                self.born_in)

    def parents(self):
        """
        Retuns a list of Person related to the current instance as parents.
        """
        return [self.mother, self.father]

    def childrens(self):
        """
        Returns a list of Person related to the current instance as childrens.
        """
        return Person.objects.filter(models.Q(mother__id=self.id) if
                self.sex == self.SEX_FEMALE_CHOICE else
                models.Q(father__id=self.id))
