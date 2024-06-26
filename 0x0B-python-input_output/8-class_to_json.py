#!/usr/bin/python3
"""Class to JSON method"""

def class_to_json(obj):
    """Returns the dictionary description with simple data structure"""
    return vars(obj)
