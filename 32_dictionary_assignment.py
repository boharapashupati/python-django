#WAP to ask subject and their mark and print their percentage and division

# output should be like 
# {'math': 55, 'english': 63, 'nepali': 45, 'percentage': 55, 'division': 'second division'}

# for i in range(1,6):
#     subject = input("Enter the subject name: ")
#     mark = int(input("Enter the mark: "))
total_student_list =[]
for student in range(2):
    subject_mark ={}
    obtain_mark= 0
    
    student_name=input("enter student name: ")
    subject_mark["name"]= student_name
    for  i in range (1,3):
        subject = input ("enter the subject name:")
        mark = input("enter the mark: ")
        subject_mark[subject] = mark
        obtain_mark =obtain_mark+int(mark)
    percentage =(obtain_mark/300)*100
    if percentage >= 80:
     division = "contralutaion! your got first division "
    elif percentage >= 60:
     division = "you got second division " 
    elif percentage >= 40:
        division = " you got Third Division"
    else :
     division = "fail"


    subject_mark["percentage"]=percentage
    subject_mark["student_name"]=student_name
    subject_mark["division"]=division
    
    total_student_list.append(subject_mark)


print(total_student_list)















