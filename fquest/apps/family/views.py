#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Description: View definitions for application 'family'.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.shortcuts import render_to_response
from models import Person


def tree(request, family_id):
    """
    Returns the necessary information to create a genealogy tree representation.
    """
    family = Person.objects.filter(family__id=family_id)

    return render_to_response('tree.html', {'family': family})

# vim:ft=python ts=4 tw=80 cc=+1:
