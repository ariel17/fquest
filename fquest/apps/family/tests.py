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
        self.d = datetime.datetime(2011, 10, 1, 15, 26)

        self.ff = Family()
        self.ff.sure_name = u"Father family's sure name"
        self.ff.leadership = Family.LEADERSHIP_PATRIARCHAL_CHOICE
        self.ff.save()

        self.father = Person()
        self.father.sex = Person.SEX_MALE_CHOICE
        self.father.name = u"Father's name"
        self.father.family = self.ff
        self.father.born_in = self.d
        self.father.save()

        self.mf = Family()
        self.mf.sure_name = u"Mother family's sure name"
        self.mf.leadership = Family.LEADERSHIP_MATRIARCHAL_CHOICE
        self.mf.save()

        self.mother = Person()
        self.mother.sex = Person.SEX_FEMALE_CHOICE
        self.mother.name = u"Mother's name"
        self.mother.family = self.mf
        self.mother.born_in = self.d
        self.mother.save()

        self.son = Person()
        self.son.name = u"Son's name"
        self.son.father = self.father
        self.son.mother = self.mother
        self.son.born_in = self.d
        self.son.family = self.ff
        self.son.save()

        self.other_son = Person()
        self.other_son.name = u"Other son's name"
        self.other_son.father = self.father
        self.other_son.mother = self.mother
        self.other_son.born_in = self.d
        self.other_son.family = self.ff
        self.other_son.save()

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
        self.son.born_in = None
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

    def test_brothers(self):
        """
        Tests the ``brothers()`` method to validate that returns other
        :model:`family.Person` instances related by parents, but not the current
        object.
        """
        self.assertTrue(self not in self.son.brothers())

    def test_parents(self):
        """
        Tests the ``parents()`` method to validate that returns other
        :model:`family.Person` instances related to the current one as parents.
        """
        parents = self.son.parents()
        self.assertEqual(2, len(parents))
        self.assertTrue(self.son.father in parents)
        self.assertTrue(self.son.mother in parents)

    def test_descendence_invalid(self):
        """
        Tests the ``descendence()`` method to validate that raises an exception
        if current instance has not sex value defined.
        """
        self.father.sex = None
        self.assertRaises(ValueError, self.father.descendence)

    def test_father_descendence(self):
        """
        Tests the ``descendence()`` method to validate that returns other
        :model:`family.Person` instances related to the current one as
        father's descendence.
        """
        d = self.father.descendence()
        self.assertEqual(2, len(d))
        self.assertTrue(self.son in d)
        self.assertTrue(self.other_son in d)

    def test_mother_descendence(self):
        """
        Tests the ``descendence()`` method to validate that returns other
        :model:`family.Person` instances related to the current one as
        mother's descendence.
        """
        d = self.mother.descendence()
        self.assertEqual(2, len(d))
        self.assertTrue(self.son in d)
        self.assertTrue(self.other_son in d)


# vim:ft=python ts=4 tw=80 cc=+1:
