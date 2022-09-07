#1. Write a Python Program to find sum of array?

class array:

    def sum_array(self,a):
        b= 0
        for i in a:
            b = b +i
        return b

#2. Write a Python Program to find largest element in an array?

    def largest_ele_array(self, a):
        b = a[0]
        for i in a:
            if b > i:
                pass
            else:
                b = i
        return b


#3. Write a Python Program for array rotation?
    def rotate_array(self,a, b):   #a is array and b is steps to be rotated
        c = []
        d = 0
        e = []
        while d < b:
            c.append(a[d])
            d = d+1

        while d>= b and d<= len(a)-1:
            e.append(a[d])
            d = d+1

        return e + c

#4. Write a Python Program to Split the array and add the first part to the end?
    def split_array(self, a):
        b = []
        for i in a:
            b.append([i])
        return b, b[0]+ b[len(b)-1]

#5. Write a Python Program to check if given array is Monotonic?
    def is_array_monotonic(self,a):
        b = []
        c = 0
        d = 0
        for i in range(len(a)-2):
            b.append(a[i+1]-a[i])

        for i in b:
            if i>0:
                c = c+1
            elif i<0:
                d = d+1
            else:
                pass
        if c == len(b):
            return "This is increasing monotonic"
        elif d == len(b):
            return "This is decreasing monotonic"
        else:
            return "this in not monotonic"






i = array()
print(i.sum_array([14,6,7]))
print(i.largest_ele_array([14,6,7]))
print(i.rotate_array([14,7,8,9,0,5], 2))
print((i.split_array([1,2,453,6,7,4,7])))
print(i.is_array_monotonic([10,8,6,4,2,1,0]))

