#warite a program to make a  algorithm calulator.

first_number = float(input("enter first number >"))
second_number = float(input("enter second number >"))
c =  input("enter your opreation")
if '+'in c:
    print(first_number+second_number)

elif'-'in c:
    print(first_number-second_number)

elif'*'in c:
  print(first_number*second_number)
  
elif'/'in c:
  if second_number != 0:
    print(first_number/second_number)
  else:
    print("zero is not divisible")
else:
   print("Invalid input")







