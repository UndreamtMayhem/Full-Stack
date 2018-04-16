from django import template

register = template.Library()


def imageurl(value): # Only one argument.
    """Converts a string into all lowercase"""
    value.split(" ")
    
    return value.lower()