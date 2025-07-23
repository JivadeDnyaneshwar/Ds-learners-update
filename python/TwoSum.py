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


num=14
step=0
while num>= 0:
    if num % 2==0:
     num=num//2
    else:
     num=num-1
    step+=1
print(step)

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
        


