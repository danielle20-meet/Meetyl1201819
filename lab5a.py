# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

import tkinter as tk
from tkinter import simpledialog


exam1 = (simpledialog.askstring("Input", "Input exam grade one: ", parent=tk.Tk().withdraw()))#asks for the grades
exam2 =(simpledialog.askstring("Input"," exam grade two: ", parent=tk.Tk().withdraw()))
exam3 =(simpledialog.askstring("Input"," exam grade three: ",parent=tk.Tk().withdraw()))
eaxm1=int(exam1)
eaxm2=int(exam2)
exam3=int(exam3)
grades = [exam1,exam2,exam3]3list of grades
sum = 0
for i in grades:
  sum = sum + int(i)
avg = sum / len(grades) #avg of grades

if (avg >= 90):
    letter_grade = "A"
elif avg>=80 and avg<=90:
    letter_grade="B"
elif avg>=70 and avg<=79:
    letter_grade="C"
elif avg>=60 and avg<=69:
    letter_grade="D"
else:
    letter_grade="F"

for grade in grades:
    print("Exam: " + str(grade))
    print("Grade: " + letter_grade)

if letter_grade == "F":
    print ("Student is failing.")
else:
    print ("Student is passing.")
print("Average: " + str(avg))