#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: View definitions for application 'family'.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import list_detail
from models import Family, Person


def tree_chart(request, family_id, restricted):
    """
    Returns the necessary information to create a genealogy tree chart
    representation, for an indicated family.
    """
    family = get_object_or_404(Family, id=family_id)

    persons = Person.objects.filter(family__id=family_id) if restricted else \
            family.roots()

    node_template = 'tree/nodes_%s.html' % ('restricted' if restricted else
            'complete')

    return render_to_response('tree/tree.html', {'family': family,
        'persons': persons, 'nodes_template': node_template,
        'restricted': restricted}, context_instance=RequestContext(request))


def family_detail(request, object_id):
    """
    Shows a family information details. Complements a generic view with related
    objects to the indicated family object.
    """
    persons = Person.objects.filter(family__id=object_id)
    return list_detail.object_detail(request, queryset=Family.objects.all(),
            object_id=object_id, extra_context={'persons': persons,})


# vim:ft=python ts=4 tw=80 cc=+1:
