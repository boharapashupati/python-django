data = '8235495'
first_number = 0
for i in data:
    if int(i)>first_number:
        first_number= int(i)
    
print("the heigest number is :", first_number)


# um1 = int(input("enter 1st number:"))
# num2 = int(input("enter 2nd number:"))
# num3 = int(input("enter 3rd number:"))

# if ( num1 <= num2) and (num1 <=num3):
#     snum = num1
# elif(num2 <= num1) and (num2 <=num3):
#     snum = num2
# else:
#     snum = num3
# print("the smallest number among12", num1,",",num2," and",num3,"is: ",snum)