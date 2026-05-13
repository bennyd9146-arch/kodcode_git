#  loops

# # 1

# for i in range(10):
#     if i % 2 == 0:
#         continue
#     if i == 7:
#         break

# print(i)

# # 2

# while True:
   
#     password = input("please enter your password: ")
    
#     if password == "1234":
#         break
   
#     else:
#         print("try again")

# print("welcome to the clube!")

# # 3

# list_products = []

# while True:
    
#     product = input("please enter your first product name: ")
    
#     if product == "done":
#         break
    
#     else:
#         list_products.append(product)


# print(list_products)


# # 3(a)

# for row in range(1,4):
    
#     for col in range(1,4):
       
#         print(f"the row is {row} and the col is {col}")
#         if col == 2:
#             break


# # 4

# str = input("please enter your str: ")
# vowels =[]
# count = 0
# for char in str:
#     if char in "aeiouAEIOU":
#         vowels.append(char)
#         count += 1


# print(f"There are {count} vowels in the string and they are {vowels}.")   

# # 5
# for i in range(1,6):
#     for j in range(1,6):
#         result = i * j

#         print(f"{i} x {j} = {result}")    
        
        
# # 6

# your_str = input("please enter your str: ")
# new_str = ""
# for i in your_str:
   
#     new_str = i + new_str

# print(new_str)

# # 7

# your_number = int(input("please enter your number: "))
# count = 0
# while your_number > 0:
#     tmp_number = your_number % 10
#     if tmp_number % 2 == 0:
       
#         count += 1 
        
#     your_number = your_number // 10
        
    
# print(count)

# # 8

# string = input("please enter  your str: ")

# Multiply_a_string = ""
# for char in string:
#     Multiply_a_string += char * 2

# print(Multiply_a_string)    


# # 9

# tmp_int = 0

# while True:

#     your_number = int(input("please enter your number: "))
#     if your_number == 0:
#         break
#     if your_number > tmp_int:
#         tmp_int = your_number


# print(f"the biggest number is {tmp_int}")    


# # 10

# your_str = input("please enter your str: " )

# for char in your_str:
#     if char.isalpha()  or char in "1234567890" :
#         continue

#     else:
#         print(False)
#         break   

# else:
#     print(True)        
        


# # 11

# tmp_int = 0
# your_number = int(input("please enter your number: "))

# while True:
#     tmp_int += your_number %10

#     your_number = your_number // 10
#     if your_number == 0:
#         break
#     tmp_int *= 10

# print(tmp_int)    
