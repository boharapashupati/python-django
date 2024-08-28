#write a program to find  lowest number amonges "82435731349"

number = "82435749"

number = [int(digit) for digit in number]
lowest_number =  min(number)
print("The lowest number is:", lowest_number)



data = "56342765721"
lowest_number = 9
for number in data :
    number=  int(number)

    if  number <lowest_number:
        lowest_number =number

        print("the lowest numberis")