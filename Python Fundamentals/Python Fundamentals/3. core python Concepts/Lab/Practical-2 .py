"""
Practical Example: How does the python code structure work?
"""

# 1. Imports (if needed)
import math   # (just to show import, not really needed here)

# 2. Variables
student_name = "Ashwin"
marks = [85, 90, 78, 92, 88]  # List of marks in 5 subjects

# 3. Processing with loops
total = 0
for mark in marks:
    total += mark

average = total / len(marks)

# 4. Conditional logic
if average >= 90:
    grade = "A+"
elif average >= 75:
    grade = "A"
elif average >= 60:
    grade = "B"
else:
    grade = "C"



# 6. Output

print("----- Student Report -----")
print("Name:", student_name)
print("Marks:", marks)
print("Average:", average)
print("Grade:", grade)

