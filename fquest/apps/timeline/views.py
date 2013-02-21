#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: View definitions for application 'event'.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from models import Event
from django.shortcuts import render_to_response


def events(request):
    """
    Shows the time line as consecutive secuence of events.
    """
    events = Event.objects.all()
    return render_to_response('timeline.html', {'events': events})

# vim:ft=python ts=4 tw=80 cc=+1:
