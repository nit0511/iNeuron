#5. Write a Python Program for cube sum of first n natural numbers?

n = 6
b = 0
c = []

for i in range(n):
    b = i**3 + b
    c.append(i**3)

print(b , c)

