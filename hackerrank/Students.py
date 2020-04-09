# Student received a , and the next multiple of from is . Since , the student's grade is rounded to
# .
# Student
# received a , and the next multiple of from is . Since , the grade will not be modified and the student's final grade is
# .
# Student
# received a , and the next multiple of from is . Since , the student's grade will be rounded to
# .
# Student
# received a grade below , so the grade will not be modified and the student's final grade is .
import math

def gradingStudents(grades):
    # Write your code here
    grades_rounded = []
    for i in grades:
        if (math.ceil(i /5)*5) - i < 3 and i >= 38:
            grades_rounded.append(math.ceil(i /5)*5)
        else:
            grades_rounded.append(i)
    return grades_rounded
                
list = [4,73,67,38,33]
for i in gradingStudents(list):
    print(i)























