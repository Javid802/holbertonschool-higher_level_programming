#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number > 0 or str(number)[-1] == "0":
    sign = ''
else:
    sign = '-'
last = sign + str(number)[-1]
print(f"Last digit of {number} is {last} and", end = "")
if last > "5":
    print("is greater than 5")
elif last == "0":
    print("is 0")
else:
    print("is less than 6 and not 0")
