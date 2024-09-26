from math import floor

students = int(input("How many students: "))
marks = []

print("Enter the marks of the students: (hit enter after each input)")
for i in range(students):
    mark = int(input("-- "))
    marks.append(mark) #.append adds the value of 'mark' at the end of the list 'marks'

average = floor(sum(marks) / students)

print("Yalls average is ",average)
if average <= 50:
    print("wtf step that pace up")
elif average > 50 and average <= 85:
    print("Not bad tbh (could improve...like a lot)")
else:
    print("Nice")
