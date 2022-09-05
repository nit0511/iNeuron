#4. Write a Python Program To Find ASCII value of a character?

import logging
logging.basicConfig(filename= "Programming Assignment_5.4.log", level= logging.DEBUG)

def ASCII_val_char(a):
    b = ord(a)
    return b

a = ASCII_val_char('C')
print(a)

