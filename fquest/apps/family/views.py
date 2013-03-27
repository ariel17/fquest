#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: View definitions for application 'family'.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Family, Person
from django.views.generic.base import View


class TreeChartView(View):
    """
    View class implementing how tree charts must fetch required information to
    display in template.
    """

    __TEMPLATE_NAME_FORMAT = 'tree/nodes_%s.html'

    NODE_COMPLETE_TEMPLATE = __TEMPLATE_NAME_FORMAT % 'complete'

    NODE_RESTRICTED_TEMPLATE = __TEMPLATE_NAME_FORMAT % 'restricted'

    TREE_TEMPLATE = 'tree/tree.html'

    restricted = None

    def get(self, request, *args, **kwargs):
        """
        Renders the content for a GET request.
        """
        family_id = kwargs['family_id']

        family = get_object_or_404(Family, id=family_id)
                                                                                   
        persons = Person.objects.filter(family__id=family_id) \
                if self.restricted else family.roots()
                                                                                   
        node_template = self.NODE_RESTRICTED_TEMPLATE if self.restricted else \
                self.NODE_COMPLETE_TEMPLATE
                                                                                   
        return render_to_response(self.TREE_TEMPLATE, {
            'family': family,
            'persons': persons,
            'nodes_template': node_template,
            'restricted': self.restricted
            }, context_instance=RequestContext(request))


# vim:ft=python ts=4 tw=80 cc=+1:
