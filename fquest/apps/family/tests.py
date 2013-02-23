#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tests classes for application 'family'.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


import datetime
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

        self.d = datetime.datetime(2011, 10, 1, 15, 26)

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

    def test_is_alive_not_defined(self):
        """
        Tests the return value when a Person hasn't defined a born date nor a
        deceased date.
        """
        self.assertIsNone(self.son.is_alive())

    def test_is_alive_not_alive(self):
        """
        Tests the return value when a Person is dead, based on the object
        dates.
        """
        self.son.born_in = self.d
        self.son.deceased_in = self.d
        self.assertFalse(self.son.is_alive())

    def test_is_alive_alive(self):
        """
        Tests the return value when a Person is dead, based on the object
        dates.
        """
        self.son.born_in = self.d
        self.assertTrue(self.son.is_alive())


# vim:ft=python ts=4 tw=80 cc=+1:
