# subject = {
#     "math" :54,
#     "nepali" :78,
#     "secince" :98,
#     "english" :90
#     }
# #print(subject["math"])
# for key in subject :
#     #print(subject[key])
#   print(f"your mark in{key} is {subject[key]}")


#WAP to ask subject and their mark and print their percentage and division

num_subjects = {"math","nepali","social","english","computer","account"}
total_marks = 0 #start with zero 

for i in range(1,6):
 
    mark = int(input(f"enter the marks for subjects {i+1}:"))
    total_marks += mark
     
print(f"Total Marks:", total_marks/6 * 100)

percentage = (total_marks/(6 *100))*100
print(f"Percentage: {percentage:.2f}%")
    
    
if percentage >= 80:
 divison = "contralutaion! your got first division "

elif percentage >= 60:
 division = "you got second division " 

elif percentage >= 40:
    division = " you got Third Division"
else :
 divison = "fail"
print(f"division: {division}")


