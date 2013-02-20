#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Description: Admin class for 'person' applications' models.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.contrib import admin
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from models import Family, Person


class FamilyAdmin(admin.ModelAdmin):
    """
    The administration class for model Family.
    """
    list_display = ['id', 'sure_name_admin']

    def sure_name_admin(self, obj):
        """
        """
        tree_url = reverse('family_tree', args=[obj.id])
        return "<a href='%s'>%s</a>" % (tree_url, obj.sure_name)
                                                                           
    sure_name_admin.allow_tags = True


admin.site.register(Family, FamilyAdmin)


class PersonAdmin(admin.ModelAdmin):
    """
    The administration class for model Person.
    """
    fieldsets = (
            (_('About his identification'), {
                'classes': ('extrapretty',),
                'fields': ('name', 'family', 'sex')
            }),
            (_('About his lifetime dates'), {
                'classes': ('extrapretty',),
                'fields': ('born_in', 'deceased_in')
            }),
            (_('About his parents'), {
                'classes': ('extrapretty',),
                'fields': ('mother', 'father')
            }),
        )
    list_display = ['id', 'name', 'sure_name_admin', 'sex', 'born_in',
            'deceased_in', 'parents_admin']
    list_display_links = ['id', 'name']
    list_filter = ['family', 'sex']

    def parents_admin(self, obj):
        """
        Returns an HTML string with links to the parent Person objects.
        """
        names = ""
        for p in obj.parents():
            if p is None:
                continue

            if names != "":
                names += ", "

            admin_url = reverse('admin:%s_%s_change' % (p._meta.app_label,
                p._meta.module_name),  args=[p.id])

            names += "<a href='%s'>%s %s (%s)</a>" % (admin_url, p.name,
                    p.family.sure_name, p.sex)

        return names

    parents_admin.short_description = 'Parents'
    parents_admin.allow_tags = True

    def sure_name_admin(self, obj):
        """
        """
        admin_url = reverse('admin:%s_%s_change' % (obj.family._meta.app_label,
                obj.family._meta.module_name),  args=[obj.family.id])
        return "<a href='%s'>%s</a>" % (admin_url, obj.family.sure_name)
                                                                           
    sure_name_admin.short_description = _('Sure Name')
    sure_name_admin.allow_tags = True


admin.site.register(Person, PersonAdmin)
