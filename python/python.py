# # x=1 #integer
# # print(x)


# a=10
# b=20
# c=a+b

# print(a+b)
# print(a-b)
# print(a*b)
# print(a%b)
# print(a/b)

# marks=[12,23,32,38]

# x=marks[1:]
# x=marks[-2:]
# x=marks[:-1]
# print(x)

# marks.append(99)
# print(marks)
# marks.pop(0)
# print(marks)

# x=[2,1,3,2]
# x.sort()
# print(x)
# x.sort(reverse=True)
# print(x)

# tup=(43,98,90,53,36)
# # print(tup)
# # tup.index(43)
# x=tup.count(36)
# print(x)


# movies=[]
# mov1=input("Enret the Movies Name:")
# mov2=input("Enter the second movies Name:")
# mov3=input("Enter the thread movies:")

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)


# palin = [1, 2, 1]
# copy=palin.copy()
# copy.reverse()   


# if copy == palin:
#     print("is a palindrom")
# else:
#     print("is a no palindrom")

# grades=["C","A","B","A","A"]
# count_A=grades.count("A")
# print("Number of a Grades:",count_A)

# grades.sort()
# print("Sordet Greades:",grades)


# nums = [23, 12, 8, 45, 60]

# for num in nums:
#     if num % 2 == 0:
#         print(f"{num} is Even")
#     else:
#         print(f"{num} is Odd")


# nums = [23, 12, 8, 45, 60]

# even_count=0
# if nums[0]%2==0:
#     even_count=even_count+1
# if nums[1]%2==0:
#     even_count=even_count+1
# if nums[2]%2==0:
#     even_count=even_count+1
# if nums[3]%2==0:
#     even_count=even_count+1
# if nums[1]%2==0:
#     even_count=even_count+1
#     print(even_count)    


# Student={
#     "Name":"Dnyanu",
#     "Age":21,
#     "marks":[80,95,70]
# }

# print(Student["Name"])
# print(Student["Age"])
# print(Student["marks"])
# Student["Age"]=22
# Student["College"]="pvp College"
# print(Student)
# print(Student.keys())
# print(Student.values())
# print(Student.items())
# print(Student.get("Name"))
# Student.update({"Age":29})
# print(Student)


# s={"python","Java"}

# s.add("C++")
# s.remove("python")
# s.discard("Java")
# print(s)
# s.clear()
# print(s)

# s.pop()
# print(s)

# a={1,2,3,4}
# b={1,2,3,4}
# print(a.union(b))
# print(a.intersection(b))

# dis={
# "cat":"a small animal","hhchhcc"
# "table":["a piece of furniture","list of facts & figures"]

# }
# print(dis)

# set={"python","java","C++","python","javascript","java","python","java","C++","C"}
# print(set)

# print(len(set))

# marks={}
# mark=input("Enter the 1 marks:")
# mark=input("Enter the 2 marks:")
# mark=input("Enter the 3 marks:")
# marks.update({"Java":mark})
# marks.update({"python":mark})
# marks.update({"C++":mark})
# print(marks)


# set={("int",9),("duble",9.0)}
# print(set)


# num=72
# if num>0:
#    if num%2==0:
#       print("Positive Even Number")
#    else:
#       print("Positive odd Number")
# else:
#    print("Number is not positive")      


# Age=20
# country="India"
# if Age>=18 and country=="India":
#     print("Eligible to vote in india")

# ternary oprator
# a=10
# b=20
# greater=a if a>=b else b
# print("Greater number is:",greater)



# pass statment
# x=5
# if x>3:
#     pass
#     print("continue with the program")


# Leap year
# year=int(input("Enter the year:"))
# if(year%4==0)and(year%100!=0)or(year%400==0):
#     print("it is Leap year",year)
# else:{
# print(" it is not Leap year",year)
# }


#  Find the Greatest of 3 Numbers
# a=int(input("Enter first number:"))
# b=int(input("Enter second number:"))
# c=int(input("Enter third number:"))
# if a>=b and a>=c:
#   print("Greatest number is:",a)
# elif b >= a and b>=c:
#  print("Greatest number is:",b)
# else:
#   print("Greatest number is:",c)


# Check if a Number is Positive,Negative,or Zero:
# num=int(input("Enter a number:"))
# if num>0:
#  print("The number is Positive")
# elif num==0:
#  print("The number is Zero")
# else:
#  print("The number is Negative")

#  Voter Eligibility
# age = int(input("Enter your age: "))
# if age >= 18:
#  print("You are eligible to vote.")
# else:
#  print("You are not eligible to vote.")


#  Ask the user to enter a light color (red/yellow/green) and print the appropriate action
#  (Stop, Slow Down, Go)

# light = input("Enter the traffic light color (red/yellow/green): ").lower()
# if light == "red":
#  print("Stop")
# elif light == "yellow":
#  print("Slow Down")
# elif light == "green":
#  print("Go")
# else:
#  print("Invalid color entered.")




