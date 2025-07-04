# prior knowledge:
#    Control Flow
#    Boolean values
#    Comparision operators

# Write a program that requires input of an integer between 0 and 1000,
# Telling user is that bigger or smaller than the **target value**
# Once they guessed the number correctly, congratulate to them.


# Start code, don't modify
from random import randint

target = randint(0, 1000)

# You go with an integer `target` in [0, 1000]
# Phase two: based on your code in `controlflow.py`, limit maximium tries.
# Hint: for _ in ...:, else:
