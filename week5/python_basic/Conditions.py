# x = "5"
# y = 3
# print(x * y)
# print(x + y)

# x = True
# print(x + x)

# print(x * 7)

# print(isinstance(True,float))
# print(type(isinstance))

# 1

# print(3 % 2 == 0)

# # 2
# x = 5 
# y = 6
# x = x + y
# y = x - y
# x = x - y
# print(x ,y)

#3
# num = 123 
# num1 = num // 100
# num2 = num // 10 % 10
# num3 = num % 10
# print(num1 + num2 + num3)

# 4
# weight = 70 
# height = 1.71
# BMI = weight / (height)**2
# newBMI = BMI * 100
# tmp = int(newBMI)
# BMI = tmp / 100
# print(BMI)

# num = 15.5




# # 5
# num1 = int(num)
# num2 = num - num1
# print(f"the integer number is {num1} and the float number is {num2}")


# conditions

# # 1

# age = int(input("please enter your age : "))
# if 0 > age or age > 120:
#     print("invalid")

# elif 0 <= age <= 12:
#     print("Child")

# elif 13 <= age <= 17:
#     print("Teen")

# else:
#     print("Adult")


# # 2

# char = input("please enter your chair : ")
# if not char.isalpha():
#     print("Invalid")

# elif char in "aeiou":
#     print("Vowel")

# else:
#     print("Consonant")
    
# # 3

# age = int(input("please enter your age : "))
# if age < 18:
#     print("No entry")



# elif 18 >= age <= 20:

#     VIPcard = input("please enter if you have a VIPcard (yes/no):")

#     if VIPcard == "yes":
#         print("Entry approved")

#     else:
#         print("No entry")       

# elif 21 >= age <= 24:
#     print("Entry approved")


# else:
#     print("No entry")

# #4

# code = 12345678

# password = input("plesae enter your passsword : ")

# if password == code:
#     print("Access Granted")

# elif len(password) < 8 :
#     print("Too short")

# else:
#     print("Wrong password")



# # 5

# x = int(input("please enter your coordinate for x : "))
# y = int(input("please enter your coordinate for y : "))


# if x > 50 or x < 10 or y < 20 or  y > 80:
#     print("Outside the rectangle")

# elif 10 < x < 50 and 20 < y < 80:
#     print("Inside the rectangle")


# elif (x == 10 or x == 50) or (y == 20 or y == 80):
#     print("On the edge")

# #6

# name = input("please enter your name : ")
# print(f"your name is {name or "Anonymous"}")

# #7

# num1 = int(input("please enter your first number : "))
# num2 = int(input("please enter your second number : "))
# num3 = int(input("please enter your third number : "))

# positive_count = ((num1 > 0) + (num2 > 0) + (num3 > 0))
# print(positive_count)

# # 8

# score = int(input("please enter your score : "))

# result = "A" if 90 <= score <= 100 else "B" if 90 > score >= 80 else "C" if 80 > score >= 70 else "F" if score < 70 else "error"

# print(result)




