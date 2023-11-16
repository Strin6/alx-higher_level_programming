#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # Combine both sets to find all unique elements
    all_elements = set_1.union(set_2)

    # Find elements that are exclusive to each set
    only_diff_set = set()
    for element in all_elements:
        if (element in set_1) ^ (element in set_2):
            only_diff_set.add(element)

    return only_diff_set
