#!/usr/bin/python3

def lookup(obj):
    # Get all attributes and methods of the object
    all_attributes_and_methods = dir(obj)

    # Filter out the attributes and methods that start with underscores
    filtered_attributes_and_methods = [attr for attr in all_attributes_and_methods if not attr.startswith('_')]

    return filtered_attributes_and_methods
