# if
# elsif
# else

# age = 18
# if age >18:
#     print("you can vote")

# age = 10
# if age >18:
#     print('you are adult')
 
# else:
#     print("you are not adult ")

    
#wap to take user input mark percentage and print their divisio .


# mark = input("enter your mark percentage")
# mark = int(mark)
# if mark<30:
#     print("fail")
# elif mark<40 :
#     print("third divison")
# elif mark<60 :
#     print("second divison")
# elif mark<80 :
#     print("first divison")
# else :
#     print("distincation")
    
    
    
# age = input("enter your age")
# age = int(age)
# if age>0 and age<12:
#   print("you are child")
# elif age>12 and age < 20:
#     print("you are teen ager")
# elif age>20 and age<50:
#     print("you are adult")
# elif age>=50:
#     print("you are old")



#wap to take use input tempreature .
# "todya is very cold "
# "today is noraml "
# "today is vey hot"

# teamperature = int(input("Enter the teamperature today"))
# 
# if teamperature <10:
#     print("today is very cold")
# elif 10 <= teamperature <= 25:
#     print("today is normal")
# else:
#     print("today is very hot")
    
    
    #WAP to take length and breadth of your house and calculate area of rectangle.

# length = float(input("Enter the length of your house :"))
# breadth = float(input("Enter the breadth of your house :"))
# area = length * breadth
# print(f"The area of your house is {area} square meters.")

#WAP to cp price,sp price and calculate profit and loss

cp = int(input("enter the your cost price :"))
sp = int(input("enter your selling price: "))
if sp > cp :
    profit = sp-cp
    print(f"profit:${profit}")
elif cp > sp:
     loss =cp-sp
print(f"loss:${loss}")
else:
print("no profit,no loss.")

#WAP to take user input number and print that number is odd or even.

# Number = int(input("enter your number"))
# remainder = Number%2
# if remainder == 0:
#     print(Number,"is even number")
# else:
#     print(Number,"is odd number")


#WAP to take user input number and print that number is prime or composite.

num = int (input("enter a number "))
for i in range(2,num):
    if (num %i) == 0:
        print(num,"is a composite number.")
        break
    else:
        print(num,"this number is prime ") 
else:
        print(num,"this number is not prime ")  