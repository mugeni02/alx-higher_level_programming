#!/usr/bin/python3
"""
================================
Module with method add_attribute
=================================
"""
def add_attribute(obj, attr_name, attr_value):
    """Add a new attribute to an object if possible."""
    if hasattr(obj, '__dict__'):
        obj.__dict__[attr_name] = attr_value
    else:
        raise TypeError("can't add new attribute if the object can’t have new attribute")

