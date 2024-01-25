#!/usr/bin/python3

def common_elements(set_1, set_2):
    """returns a set of common elements in two sets.
    @set_1: set to be compared
    @set_2: set to be compared
    """
    comm_elem = []

    for elem in set_1:
        if elem in set_2:
            comm_elem.append(elem)

    return comm_elem

#alternatively,
#def common_elements(set_1, set_2):
    return(set_1 & set_2)
