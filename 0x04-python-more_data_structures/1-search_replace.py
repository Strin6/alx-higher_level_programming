Write a function that replaces all occurrences of an element by another in a new list.

Prototype: def search_replace(my_list, search, replace):
my_list is the initial list
search is the element to replace in the list
replace is the new element
You are not allowed to import any modul


#!/usr/bin/python3
    def search_replace(my_list, search, replace):
        new_list = list(map(lambda x: replace if x == search else x, my_list))
        return new_list
