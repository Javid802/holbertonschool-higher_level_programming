#!/usr/bin/python3
def print_last_digit(number):
    if number<0:
        print(-1 * int(str(number)[-1]), end="")
    else:
        print(int(str(number)[-1]), end="")