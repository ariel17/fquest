#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: View definitions for application 'event'.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from models import Event
from fquest.apps.family.models import Family


def events(request, family_id, template):
    """
    Shows the time line as consecutive secuence of events.
    """
    family = get_object_or_404(Family, id=family_id)
    events = Event.objects.filter(persons__family__id=family_id)

    p_from = request.GET.get('from', None)
    if p_from:
        events = events.filter(occurred_in__gt=p_from)

    p_to = request.GET.get('to', None)
    if p_to:
        events = events.filter(occurred_in__lt=p_to)

    return render_to_response(template, {'family': family, 'events': events})


# vim:ft=python ts=4 tw=80 cc=+1:
