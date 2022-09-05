#5. Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?

import logging
logging.basicConfig(filename= "Programming Assignment_5.5.log", level= logging.DEBUG)

class MathematicalOperation:

    def sum(self, *a):
        print(a)

        b = 0
        for i in a:
            b = i+b
        return b

    def subs(self, a, b):
        c = a-b
        return c

    def division(self, a, b):
        c = a/b
        return c

    def multiplication(self,a, b):
        c = a*b
        return c

calculator = MathematicalOperation()
sum = calculator.sum(5,3,4,5,7)
print(sum)
logging.info(sum)

minus = calculator.subs(10, 20)
print(minus)
logging.info(minus)

multi = calculator.multiplication(10, 20)
print(multi)
logging.info(multi)

div = calculator.division(10, 20)
print(div)
logging.info(div)

