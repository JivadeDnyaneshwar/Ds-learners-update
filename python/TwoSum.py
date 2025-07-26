#  #Swap Two Numbers Without Using a Third Variable
# a=10
# b=7
# a=a+b
# b=a-b
# a=a-b
# print("a:",a)
# print("b:",b)

 #Calculate the Area of a Circle
# radius=5
# area=3.14*radius*radius
# print("Calculate the Area of a Circle:",area)


#  Check if a Number is Positive, Negative, or Zero

# num=int(input("Enter the Number:"))
# if num > 0:
#     print("Number is Positive:")
# elif num == 0:
#     print("Number is Zero:")
# else:
#     print("Number is Negative:")    


#  Identify the Character Type

# char=input("Enter the Charactor:")
# if char.isalpha():
#     if char.lower()in'aeiou':
#         print("Vowel")
#     else:
#         print("Consonent")
# elif char.isdigit():
#     print("Digit")
# else:
#     print("Special Char")


#  Find the Smallest of Three Numbers

# sum of number
# sum=int(input("Enter the Number:"))
# s=0
# i=1
# while i<=sum:
#     s+=i
#     i+=1
#     print("Sum",s)

# Sum of natural numbers up to n

# n = int(input("Enter the number: "))
# sum = 0
# i = 1

# while i <= n:
#     sum += i
#     i += 1

# print(" sum ", sum)






# # Continue Statement

# x = 0
# while x < 5:
#     x += 1
#     if x == 3:
#         continue
#     print(x)



# # Break Statement

# x = 1
# while x < 10:
#     if x == 5:
#         break
#     print(x)
#     x += 1


# # Print numbers from 10 to 1 using a while loop
# i = 10
# while i >= 1:
#     print(i)
#     i -= 1



# even numbers
# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print(i)
#     i += 1






# # simple password checker

# correct_password = "0010"
# password = input("Enter password: ")
# while password != correct_password:
#     password = input("Incorrect. Try again: ")
# print("Access granted")




# num=int(input("Enter the Number:"))
# n1,n2=0,1
# print(n1,n2,end=" ")
# for i in range(2,num):
#     n3=n1+n2
#     n1=n2
#     n2=n3
#     print(n2,end=" ")


#num=14
# steps=0
# while num > 0:
#     if num % 2==0:
#         num = num//2

#     else:
#         num = num - 1
#     steps +=1
# print(steps)

# num=877
# step=0
# while num>=10:
#     temp=num
#     sum_digit=0
#     while temp>0:
#         sum_digit += temp%10
#         temp=temp//10
#     num=sum_digit
#     step+=1
# print(step)
        


# function
# def addnum(a,b):
#     c=a+b
#     print(c)
# addnum(2,3)
# addnum(5,6)
#  parameter and argument //opgisnol argument

# def greet(Name,Age):
#     print(f"Hi,I am {Name},and I am {Age} years old.")
# greet("Dnyanu",21)

# local vs global
# Local function cha Aat
#  global function cha baher
# x=10
# def func():
#     x=5
#     print("Local X:",x) 
# func()
# print("Global x:",x)   

# lamda function
# square=lambda x:x*x
# print(square(4))


# num=int(input("Enter the Number:"))
# n1,n2=0,1
# print(n1,n2,end=" ")
# for i in range(2,num):
#     n3=n1+n2
#     n1=n2
#     n2=n3
#     print(n2,end=" ")

# def nesse(num):
#       n1, n2 = 0, 1
#       print(n1, n2, end=" ")
#       for i in range(2, num):
#         n3 = n1 + n2
#         n1 = n2
#         n2 = n3
#         print(n2, end=" ")

# num = int(input("Enter the vluve: "))
# nesse(num)


# def add(num):
#     steps = 0
#     while num > 0:
#         if num % 2 == 0:
#             num = num // 2
#         else:
#             num = num - 1
#         steps += 1
#     return steps
# num = 14
# print(add(num))

# default argument
# def defa(name="Dnaynu"):
#     print("Hello "+name)
# defa("Mahesh")    
# defa()


#  Key world argument
# def keyw(name,age):
#     print(name+" is "+str(age)+" years old")
# keyw(age=21,name="Dnyanu")    


# Required [positional] argu
# def multi(a,b):
#     return a*b
# print(multi(3,2))

# converting to float
# type casting
# int_value=100
# string_value="1.5"
# float_value=float(int_value)
# print("int value as a float:",float_value)
# print(type(float_value))
# float_value=float(string_value)
# print("String_value as a fload: ",float_value)
# print(type(float_value))


# variable argu
# *args
# def total(*number):
#     sum=0
#     for num in number:
#         sum+=num
#     print("Sum:",sum)
# total(1,2,3,4)


# **kwargs 
# ** key value madhe data gheycha ahe toho use karto
# def show_details(**names):
#     for key,value in names.items():
#          print(f"{key}:{value}")
# show_details(Name="Dnyanu",Age=21,city="Loni")         
   

        

# function use largest number

# def max_in_list(list):
#     return max(list)
# print(max_in_list([2,3,4,7,1]))


# no using function
# num_max=[80,9,8,6]
# num_of_max=max(num_max)
# print("Max Number:",num_of_max)


# def max_in_list(list):
#     return max(list)
# print(max_in_list([2,3,4,7,1]))


    
# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a

# # Example usage
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# result = gcd(num1, num2)
# print(f"The GCD of {num1} and {num2} is {result}")


import math
a=12
b=18
print(math.gcd(a,b))