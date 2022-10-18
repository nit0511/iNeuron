#1. Write a Python Program to Add Two Matrices?
def blank_matrix_for_sum(a):
    c = []
    for i in range(len(a)):
        d = []
        for j in range(len(a[0])):
            d.append(0)
        c.append(d)
    return c

def blank_matrix_for_multiplication(a, b):
    c = []
    for i in range(len(a)):
        d = []
        for j in range(len(b[0])):
            d.append(0)
        c.append(d)
    return c


class matrix:
    # 1. Write a Python Program to Add Two Matrices?
    def matrix_sum(self, a,b):
        c = blank_matrix_for_sum(a)

        for i in range(len(a)):
            for j in range(len(a)):
                c[i][j] = a[i][j]+b[i][j]
        return c
#2. Write a Python Program to Multiply Two Matrices?
    def matrix_multiplication(self, a, b):
        c = True
        while c == True:
            if len(a) == len(b[0]) and len(b) == len(a[0]):
                c = False
            else:
                print("please enter valid matrix for multiplication")

        #d = blank_matrix_for_multiplication(a,b):
        d = blank_matrix_for_multiplication(a,b)
        for i in range(len(a)):

            for j in range(len(b[0])):
                e = 0
                for k in range(len(b[0])):
                    e = a[i][k]*b[k][j] + e
                d[i][j] = e


        return d
#3. Write a Python Program to Transpose a Matrix?
    def transpose_of_matrix(self, a):
        b = []
        for i in range(len(a[0])):
            c = []
            for j in range(len(a)):
                c.append(a[j][i])
            b.append(c)
        return b





i = matrix()
a = [[1,2,3],[4,5,6],[7,8,9]]
b = [[10,11,12],[13,14,15],[16,17,18]]
i.matrix_sum(a,b)
print(i.matrix_sum(a,b))
print(i.matrix_multiplication(a,b))
print(i.transpose_of_matrix(a))

#4. Write a Python Program to Sort Words in Alphabetic Order?

words = [Nitesh, Abhimanyu, Ajay, Seema, Yashwant, Nitin, Surya, Jayesh, Rohit, Aastha, Alwin, Kuladeep]
