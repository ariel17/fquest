#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.test import TestCase
from models import Family, Person


class PersonTest(TestCase):
    """
    Tests the behaviour of class Person.
    """

    def setUp(self):
        """
        Initialize needed resources.
        """
        self.ff = Family()
        self.ff.sure_name = u"Father family's sure name"
        self.ff.leadership = Family.LEADERSHIP_PATRIARCHAL_CHOICE

        self.father = Person()
        self.father.name = u"Father's name"
        self.father.family = self.ff

        self.mf = Family()
        self.mf.sure_name = u"Mother family's sure name"
        self.mf.leadership = Family.LEADERSHIP_MATRIARCHAL_CHOICE

        self.mother = Person()
        self.mother.name = u"Mother's name"
        self.mother.family = self.mf

        self.son = Person()
        self.son.name = u"Son's name"
        self.son.father = self.father
        self.son.mother = self.mother

    def test_family_leader_patriarchal(self):
        """
        Must return the correct family leader based patriarchal configured
        leadership.
        """
        self.son.family = self.ff
        self.assertEqual(self.son.family_leader(), self.father)

    def test_family_leader_matriarchal(self):
        """
        Must return the correct family leader based matriarchal configured
        leadership.
        """
        self.son.family = self.mf
        self.assertEqual(self.son.family_leader(), self.mother)

    def test_family_leader_not_defined(self):
        """
        Must return a None object when the leadership is not defined.
        """
        self.son.family = self.mf
        self.son.family.leadership = None
        self.assertIsNone(self.son.family_leader())









# vim:ft=python ts=4 tw=80 cc=+1:
