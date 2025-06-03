#TASK 7: Using Python or PHP or Java or Ruby or JavaScript
#Write that prompts the user to input student marks. The input should be between 0 and 100.Then output the correct grade: 
#A > 79 , B - 60 to 79, C  > 49 to 59, D - 40 to 49, E - less 40
#Once you learn functions,revisit this and write this code inside a function.

student_marks=input("enter student marks: ")
student_marks=int(student_marks)

if student_marks>79:
    print("A")
elif student_marks>59<80:
    print("B")
elif student_marks>49<60:
    print("C")
elif student_marks>39<50:
    print("D")
elif student_marks<40:
    print("E")
else:
    print("Fail")