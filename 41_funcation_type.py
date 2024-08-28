#write a program to make calculator ,make funcation of each  opertor.
def add(a,b):
    print(a+b)
def subtract(a,b):
    print(a-b)
def multply(a,b):
    print(a*b)        
a = int(input("enter your first number: "))
b = int(input("enter your second number: "))
r = input("enter your operatpr: ")
if '+'in r:
    add(a,b)
elif '-'in r:
    subtract(a,b)
elif '*' in r:
    multply(a,b)
else:
    print("Invalid operator. Please enter +, -, or *.")
    
    
    