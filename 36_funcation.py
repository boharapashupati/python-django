# funcation is block of code
# def design(design_value):
#     print("this is design")
#     print(design_value)


# design("**********")
# design("&&&&&&&&&&&&&&")
# design("###################")

# def second_design():
#  print("this is design")
# print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

# def third_design():
#  print("this is design")
# print("#########################################3")

# make calculator using funcation.
# def add(a,b):
#  print(a+b)
# def subtract(a,b):
#  print(a-b)
# def multply(a,b):
#  print(a*b)    
# a = int(input("enter your first number: "))
# b = int(input("enter your second: "))
# c = input("enter your opretor: ")
# if '+'in c:
#  add(a,b)
# elif '-'in c:
#  subtract(a,b)
# elif '*' in c :
#     multply(a,b)\
    
    
#write a program  to find give value is odd or even,must include funcation #assiment.
# def is_odd_even():
#     num = int(input("enter your number:"))
#     remainder = num%2
#     if remainder == 0:
#         print("is even number")
#     else:
#         print("is odd number")
        
# is_odd_even()


# def add_number(s,b):
#         sum = s+b
#         return sum
# print("sum:", add_number(7,3))



#1. Write a program using functions to find greatest of three numbers. 
# def find_greatest(a, b, c):
#     list = [a, b, c]
#     list.sort()
#     return list[-1]

# # Test the function
# a = 10
# b = 14
# c = 12
# print(find_greatest(a, b, c))


#Write a python program using function to convert Celsius to Fahrenheit. 
# def celsius_to_fahrenheit(celsius):
#     fahrenheit = (celsius * 9/5) + 32
#     return fahrenheit
# celsius = float(input("Enter temperature in Celsius: "))
# fahrenheit = celsius_to_fahrenheit(celsius)
# print("Temperature in Fahrenheit:", fahrenheit)


#How do you prevent a python print() function to print a new line at the end
import sys
sys.stdout.write("Hello, world!")