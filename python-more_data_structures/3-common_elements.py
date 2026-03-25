#!/usr/bin/python3
def common_elements(set_1, set_2):
    salam = []
    for i, z in zip(set_1,set_2):
        if i == z:
           salam.append(i)
    return(salam)
