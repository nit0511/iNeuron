#3. Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?

import logging
logging.basicConfig(filename= "Programming Assignment_5.3.log", level= logging.DEBUG)

class number_conversion_system:
    def Decimal_binary(self,a):
        b = []
        while a//2 !=0:
            if a//2 >= 1:
                c = a%2
            b.append(int(c))
            a = a/2

        b.append(1)
        b = b[::-1]
        d = ''
        for i in range(len(b)):
            d = d + str(b[i])
        d = int(d)

        return d

    def Decimal_octal(self,a):
        b = []
        while a // 8 != 0:
            c = a % 8
            b.append(int(c))
            a = a / 8

        if a//8 == 1:
            b.append(1)
        elif a//8 == 2:
            b.append(2)

        b.append(1)
        b = b[::-1]
        d = ''
        for i in range(len(b)):
            d = d + str(b[i])
        d = int(d)

        return d



i = number_conversion_system()
b = i.Decimal_binary(510)
print(b)


