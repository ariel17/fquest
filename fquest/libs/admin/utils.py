#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Description: Utilities for admin modules.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.core.urlresolvers import reverse


def persons2admin(persons):
    """
    Returns an HTML string with links to the Person's 'change' page.
    """
    names = ""
    for p in persons:
        if p is None:
            continue

        if names != "":
            names += ", "

        admin_url = reverse('admin:%s_%s_change' % (p._meta.app_label,
            p._meta.module_name),  args=[p.id])

        names += "<a href='%s'>%s %s (%s)</a>" % (admin_url, p.name,
                p.family.sure_name, p.sex)

    return names

# vim:ft=python ts=4 tw=80 cc=+1:
