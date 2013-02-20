#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"

from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

# vim:ft=python ts=4 tw=80 cc=+1:
