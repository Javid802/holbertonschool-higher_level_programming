#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for i in sorted(a_dictionary):
        soz = i
        key = a_dictionary.get(i)
        print("{}: {}".format(soz,key))
