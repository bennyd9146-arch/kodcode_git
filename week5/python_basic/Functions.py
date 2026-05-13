# Functions

# # 1

# def is_even(num):
#     return num % 2 == 0

# print(is_even(4))

# # 2

# def factorial(num):
#     tmp_num = 1
#     for n in range(1 , num + 1):
#         tmp_num *= n

#     return tmp_num

# print(factorial(5)) 


# # 3

# def count_vowels(s):
#     tmp_vowels = 0
#     for i in s:
#         if i in "AEOIUaeoiu":
#             tmp_vowels += 1
#     return tmp_vowels
# print(count_vowels("benny"))        

# # 4
# def reverse_string(s):
#     new_str = ""
#     for i in s:
#         new_str = i + new_str
#     return new_str
# print(reverse_string("benny"))   

def index(name,/,age,adress):
    print(name,age,adress)

index("benny",21,"E'lade") 

def unlimited(*iteme):
    print(*iteme)


def itemse(name,/,*,age,adress,):
    print(name,age,adress)

