# prior knowledge:
#    Control Flow
#    Boolean values
#    Comparision operators

# Write a program that requires input of an integer between 0 and 1000,
# Telling user is that bigger or smaller than the **target value**
# Once they guessed the number correctly, congratulate to them.


# Start code, don't modify
from random import randint

MIN_NUM = 0
MAX_NUM = 100

target = randint(MIN_NUM, MAX_NUM)

# You go with an integer `target` in [MIN_NUM, MAX_NUM]

# Modify this program,
# user can guess at most 10 times
# if and only if they cannot find the number, output "You lost."
