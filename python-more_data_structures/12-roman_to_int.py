#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is not str:
        return 0
    roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    cem = 0
    evvelki = 0
    for i in reversed(roman_string):
        deyer = roman[i]
        if deyer >= evvelki:
            cem += deyer
        else:
            cem -= deyer
        evvelki = deyer
    return cem
