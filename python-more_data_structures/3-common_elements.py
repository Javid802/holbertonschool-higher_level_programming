#!/usr/bin/python3
def common_elements(set_1, set_2):
    salam = []
    for i, z in zip(set_1,set_2):
        if i == z:
           salam.append(i)
    return(salam)



set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))