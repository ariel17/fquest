#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: 'family' application class definitions.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.db import models
from django.utils.translation import ugettext as _


NAME_FIELD_MAX_LENGH = 50

CHOICE_FIELD_MAX_LENGH = 2


class Family(models.Model):
    """
    Composes the family identification and defines how the leadership is
    composed.
    """

    LEADERSHIP_PATRIARCHAL_CHOICE = u'P'

    LEADERSHIP_MATRIARCHAL_CHOICE = u'M'

    LEADERSHIP_CHOICES = (
            (LEADERSHIP_PATRIARCHAL_CHOICE, _(u'Patriarchal')),
            (LEADERSHIP_MATRIARCHAL_CHOICE, _(u'Matriarchal')),
            )

    sure_name = models.CharField(_(u'Sure Name'),
            max_length=NAME_FIELD_MAX_LENGH)
    leadership = models.CharField(_(u'Leadership'),
            max_length=CHOICE_FIELD_MAX_LENGH, choices=LEADERSHIP_CHOICES,
            help_text=_(u"Select how is built the family's leadership; "
                    "patriarchal or matriarchal"))

    class Meta:
        verbose_name_plural = _(u'Families')

    def __unicode__(self):
        return unicode(self.sure_name)


class Person(models.Model):
    """
    Represents the basic information about a person. It defines aspects as name,
    sex, born and decease dates, and family belonging.
    """

    PARENT_HELP_TEXT = _(u'Select the person that will figure as parent, if '
            'it exists in database.')

    SEX_MALE_CHOICE = u'M'

    SEX_FEMALE_CHOICE = u'F'

    SEX_CHOICES = (
            (SEX_MALE_CHOICE, _(u'Male')),
            (SEX_FEMALE_CHOICE, _(u'Female')),
            )

    name = models.CharField(_(u"The person's name"),
            max_length=NAME_FIELD_MAX_LENGH)
    family = models.ForeignKey(u'Family', related_name=_(u'Family'))
    sex = models.CharField(_(u'Sex'), max_length=CHOICE_FIELD_MAX_LENGH,
            choices=SEX_CHOICES)
    born_in = models.DateTimeField(_(u'Born date'))
    deceased_in = models.DateTimeField(_(u'Decease date'), blank=True,
            null=True)
    mother = models.ForeignKey('Person', related_name=_(u'Mother'),
            blank=True, null=True, help_text=_(PARENT_HELP_TEXT))
    father = models.ForeignKey('Person', related_name=_(u'Father'),
            blank=True, null=True, help_text=_(PARENT_HELP_TEXT))
    picture = models.ImageField(_(u'Picture'), upload_to='pictures',
            blank=True, null=True)

    def __unicode__(self):
        return u"%s %s (%s) - %s" % (self.name, self.family.sure_name,
                self.sex, self.born_in)

    def family_leader(self):
        """
        Returns the family leader (mother or father), based on the leadership
        definition on class :model:`family.Family`. If it was not defined, then
        return ``None``.
        """
        if self.family.leadership == Family.LEADERSHIP_PATRIARCHAL_CHOICE:
            return self.father
        elif self.family.leadership == Family.LEADERSHIP_MATRIARCHAL_CHOICE:
            return self.mother

        return None

    def is_alive(self):
        """
        Returns ``True`` if the person is alive, based on the ``deceased_in``
        field value. If ``born_in`` or ``deceased_in`` fields wasn't defined
        then it returns ``None``.
        """
        if not self.born_in and not self.deceased_in:
            return None

        return not self.deceased_in

    def parents(self):
        """
        Retuns a list of :model:`family.Person` related to the current instance
        as progenitors.
        """
        return [self.mother, self.father]

    def childrens(self):
        """
        Returns a list of :model:`family.Person` related to the current instance
        as childrens.
        """
        return Person.objects.filter(models.Q(mother__id=self.id) if
                self.sex == self.SEX_FEMALE_CHOICE else
                models.Q(father__id=self.id))


# vim:ft=python ts=4 tw=80 cc=+1:
