#!/usr/bin/python3
def best_score(a_dictionary):
    a = 0
    ad = ''
    if a_dictionary is None:
        return None
    for i in a_dictionary:
        if a_dictionary[i] > a:
            a = a_dictionary[i]
            ad = i
    if ad != "" :
        return ad
    else:
        return "None"
