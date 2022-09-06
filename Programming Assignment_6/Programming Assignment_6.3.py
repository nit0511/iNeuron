#3. Write a Python Program to calculate your Body Mass Index?

'''We know that Sam’s weight is 16.9 kg and his height is 105.4 cm. What is Sam’s BMI?

(16.9 kg / 105.4 cm / 105.4 cm ) x 10,000 = 15.2'''

def bmi():
    weight = float(input("Please enter your weight in KG "))
    height = float(input("please enter your Height in Cm "))
    a = (weight/(height**2))*10000
    return a
a = bmi()
if a <= 18.5:
    print("your BMI is ", a ,"and this is considered as underweight")

elif a > 18.5 and a<=24.9:
    print("your BMI is ", a, "and this is considered as Normal weight")

elif a>25  and a<=29.9:
    print("your BMI is ", a, "and this is considered as overweight")

else:
    print("your BMI is ", a, "and you are suffering from obesity")
