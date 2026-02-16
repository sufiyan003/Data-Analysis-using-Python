# This project analyzes students' academic performance using NumPy.
# It calculates student-wise and subject-wise averages, identifies top performers,
# and determines pass/fail status based on average marks.

import numpy as np

marks = np.array([
    [85, 90, 88],  
    [70, 75, 72],  
    [92, 89, 95],  
    [60, 65, 70],  
    [78, 80, 82]  
])

student_avg = np.mean(marks, axis=1)

subject_avg = np.mean(marks, axis=0)


top_student_index = np.argmax(student_avg)
top_student_score = student_avg[top_student_index]

passed_students = student_avg >= 75

print("Student Averages:", student_avg)
print("Subject Averages:", subject_avg)
print(f"Top Student: Student {top_student_index + 1} with average {top_student_score}")
print("Passed Students:", passed_students)
