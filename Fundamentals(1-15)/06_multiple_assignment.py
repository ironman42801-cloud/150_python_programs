#06
"""
Multiple assignment is used to assign multiple values or single value
to a multiple variables
"""
x = y = z = 10
a, b, c = 3, 4, 5
print(x, y, z)
#output:- 10 10 10
print(a, b, c)
#output:- 3 4 5

#Real life example
#Same section students
student_1 = student_2 = student_3= "Section 1"
#Different section students
student_4, student_5 = "Section 2", "Section 3"

print(student_1, student_2, student_3)
#output:- Section 1 Section 1 Section 1
print(student_3, student_4, student_5)
#output:- Section 1 Section 2 Section 3
