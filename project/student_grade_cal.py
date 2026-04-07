# Score calculation for students

"""
attendance : 10%
assignment : 20%
midterm : 30%
final : 40%
total score = attendance  + assignment  + midterm  + final
grade : A, B, C, D, F
"""

# input : student name, attendance score, assignment score, midterm score, final score
# output : student name, total score, grade

# Define a function to calculate total score and grade
def calculate_grade(attendance, assignment, midterm, final):
    
    total_score = attendance + assignment + midterm + final

    if total_score >= 90:
        grade = "A"
    elif total_score >= 80:
        grade = "B"
    elif total_score >= 70:
        grade = "C"
    elif total_score >= 60:
        grade = "D"
    else:
        grade = "F"

    return total_score, grade


# Get input from user
student_name = input("Enter student name: ")
atten_score = int(input("Enter attendance score (0-10): "))
assign_score = int(input("Enter assignment score (0-20): "))
midterm_score = int(input("Enter midterm score (0-30): "))
final_score = int(input("Enter final score (0-40): "))

# Calculate total score and grade
result, grade = calculate_grade(atten_score, assign_score, midterm_score, final_score)

print(f"Student Name: {student_name}")
print(f"Total Score: {result}")
print(f"Grade: {grade}")