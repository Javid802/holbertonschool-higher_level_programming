#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    salam = []
    for i in set_1:
        if i not in set_2:
            salam.append(i)
    for z in set_2:
        if z not in set_1:
            salam.append(z)
    return salam
