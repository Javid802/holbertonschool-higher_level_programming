#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        a = ''
        for i in range(x):
            a = a + str(my_list[i])
        return a
    except IndexError:
        print('salam')
