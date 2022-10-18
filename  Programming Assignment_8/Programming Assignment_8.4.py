#4. Write a Python Program to Sort Words in Alphabetic Order?

my_str = "Nitesh Abhimanyu Ajay Seema Yashwant Nitin Surya Jayesh Rohit Aastha Alwin Kuladeep"
words = [word.lower() for word in my_str.split()]
words.sort()

for word in words:
    print(word)


#5. Write a Python Program to Remove Punctuation From a String?

my_str1 = "Wow! This is great. I can't beleive you did it. Wow! Wow! Wow!"

my_str2 = my_str1.split("!")
print(my_str2)
my_str3 = ""
for i in my_str2:
    my_str3 = my_str3+i
print(my_str3)





