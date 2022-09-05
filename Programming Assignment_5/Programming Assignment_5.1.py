#1. Write a Python Program to Find LCM?

import logging
from math import sqrt
logging.basicConfig(filename= "Programming Assignment_5.1.log", level= logging.DEBUG)


def prime_no(a):
    prime = int
    if a <= 1:
        return None

    for i in range(2, int(sqrt(a)) + 1):
        if (a % i == 0):
            return None
    prime = a
    return prime

#prime = prime_no(7)
#print(prime)

def prime_list(a):
    c = []
    for i in range(a):
        b = prime_no(i)
        if b != None:
            c.append(b)
    return c

#primeList = prime_list(1000)
#print(primeList)

def factor(a):
    factor_of_no = []
    c = prime_list(a)
    b = True
    d = a
    for i in c:
        while d%i == 0:
            if d%i== 0:
                factor_of_no.append(i)
            d = d/i
    factor_of_no.append(int(d))
    return factor_of_no
#factor_of_number = factor(500)
#print(factor_of_number)

def lcm(a):
    b = []
    d = {1}
    for i in a:
        c = factor(i)
        b.append(c)
        d.update((set(c)))
    #print(d)
    logging.info("calculated factor of given no. %s", b)
    e = []

    for i in d:
        L = 0
        for j in b:
            g = 0

            for k in j:
                if k == i:
                    g = g+1
            if g > L:
                L = g
        e.append([i,L])
    answer = 1

    for i in e:
        answer = i[0]**i[1] * answer
    return answer

d = lcm([256,4])
print(d)












