#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = set()
    for elements in (set_1 and set_2):
        if elements not in set_1 and set_2:
            new_set.add(elements)

    return new_set
