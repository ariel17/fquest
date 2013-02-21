#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: View definitions for application 'family'.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from models import Family, Person


def tree(request, family_id):
    """
    Returns the necessary information to create a genealogy tree
    representation, for an indicated family.
    """
    family = get_object_or_404(Family, id=family_id)
    persons = Person.objects.filter(family__id=family_id)

    return render_to_response('tree.html', {'family': family,
        'persons': persons})


# vim:ft=python ts=4 tw=80 cc=+1:
