from turtle import ScrolledCanvas


student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}

#TODO-1: Create an empty dictionary called students grades
student_grades= {}

#TODO-2: Add the grades to scores
for student in student_scores:
    score = student_scores[student]
    if score > 91:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail" 
print(student_grades)           