#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Model definition related to diagrams created by user.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.db import models
from apps.family.models import Family
from django.contrib.auth.models import User


NAME_FIELD_MAX_LENGH = 50


class Diagram(models.Model):
    """
    Contains a family tree representation.
    """

    name = models.CharField(u'Name', max_length=NAME_FIELD_MAX_LENGH)
    author = models.ForeignKey(User)
    family = models.ForeignKey(Family)
    # tree = tree_implementation

    def __unicode__(self):
        return u"<Diagram name='%s' family=%s>" % (self.name, self.family)
    

# vim:ft=python ts=4 tw=80 cc=+1:
