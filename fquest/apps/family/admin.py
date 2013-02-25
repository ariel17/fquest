#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Admin class for 'person' applications' models.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.conf import settings
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from fquest.libs.admin.utils import persons2admin
from models import Family, Person


class FamilyAdmin(admin.ModelAdmin):
    """
    The administration class for model Family.
    """
    list_display = ['id', 'sure_name', 'leadership', 'tree_admin',
            'timeline_admin']
    list_display_links = ['id', 'sure_name',]
    list_filter = ['leadership',]

    def tree_admin(self, obj):
        """
        Returns an HTML string containing the link to the family tree
        represenation.
        """
        tree_url = reverse('tree_chart_complete', args=[obj.id])
        return u"<a href='%s'>%s</a>" % (tree_url, tree_url)

    tree_admin.allow_tags = True
    tree_admin.short_description = _(u'Tree representation URL')

    def timeline_admin(self, obj):
        """
        Returns an HTML string containing the link to the family timeline
        represenation.
        """
        tree_url = reverse('events_format', args=[obj.id])
        return u"<a href='%s'>%s</a>" % (tree_url, tree_url)
                                                                      
    timeline_admin.allow_tags = True
    timeline_admin.short_description = _(u'Events representation URL')


admin.site.register(Family, FamilyAdmin)


class PersonAdmin(admin.ModelAdmin):
    """
    The administration class for model Person.
    """
    fieldsets = (
            (_(u'About his identification'), {
                'classes': ('extrapretty',),
                'fields': ('name', 'family', 'sex', 'picture')
            }),
            (_(u'About his lifetime dates'), {
                'classes': ('extrapretty',),
                'fields': ('born_in', 'deceased_in')
            }),
            (_(u'About his parents'), {
                'classes': ('extrapretty',),
                'fields': ('mother', 'father')
            }),
        )
    list_display = ['id', 'name', 'sure_name_admin', 'sex', 'born_in',
            'deceased_in', 'parents_admin', 'picture_admin']
    list_display_links = ['id', 'name']
    list_filter = ['family', 'sex']

    def parents_admin(self, obj):
        """
        Returns an HTML string with links to the parent Person objects.
        """
        return persons2admin(obj.parents())

    parents_admin.short_description = _(u'Parents')
    parents_admin.allow_tags = True

    def sure_name_admin(self, obj):
        """
        Returns a HTML string containing the parents names with links to the
        'change' page of Person model.
        """
        admin_url = reverse('admin:%s_%s_change' % (obj.family._meta.app_label,
                obj.family._meta.module_name),  args=[obj.family.id])
        return u"<a href='%s'>%s</a>" % (admin_url, obj.family.sure_name)

    sure_name_admin.short_description = _(u'Sure Name')
    sure_name_admin.allow_tags = True

    def picture_admin(self, obj):
        """
        """
        return u"<a href='%s%s'>%s</a>" % (settings.MEDIA_URL, obj.picture,
                obj.picture)
    
    picture_admin.short_description = _(u'Picture')
    picture_admin.allow_tags = True


admin.site.register(Person, PersonAdmin)


# vim:ft=python ts=4 tw=80 cc=+1:
