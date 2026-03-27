#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        a = ''
        for i in range(x):
            a = a + my_list[i]
    except IndexError:
        print('salam')
        
        
        
my_list = [1, 2, 3, 4, 5]