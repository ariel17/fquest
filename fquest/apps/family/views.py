#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Description: View definitions for application 'person'.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.shortcuts import render_to_response


def tree(request):
    """
    Returns the necessary information to create a genealogy tree representation.
    """
    return render_to_response('tree.html')
