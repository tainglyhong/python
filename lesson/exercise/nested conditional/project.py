"""
Recommends a course based on user preferences.
Category: Online Learning (Khan Academy + Tech Courses)

✔ At least 5 course options
✔ Uses multiple input() attributes (3+)
✔ Uses compound conditions + nested logic
✔ Clean, structured, and extendable
"""

# Course options (at least 5)
fin_lit = "Financial Literacy"
pixar = "Pixar in a Box"
grammar = "Grammar"
python_course = "Intro to Python Programming"
web_dev = "Web Development Basics"
data_science = "Data Science Fundamentals"

# Collect user preferences
grade = int(input("What grade are you in? "))
favorite_subject = input("What is your favorite subject? (math/art/computing/english/business): ").lower()
career_interest = input("What career are you interested in? (developer/designer/analyst/none): ").lower()
learning_style = input("Preferred learning style? (creative/logical/practical): ").lower()

# Recommendation logic
recommend = ""

# Condition group 1: Younger students
if grade < 6:
    if learning_style == "creative" and favorite_subject == "art":
        recommend = pixar
    else:
        recommend = grammar

# Condition group 2: Middle/High school
elif grade >= 6 and grade <= 12:
    if (favorite_subject == "computing" or career_interest == "developer"):
        if learning_style == "logical":
            recommend = python_course
        else:
            recommend = web_dev
    elif favorite_subject == "math" and career_interest == "analyst":
        recommend = data_science
    else:
        recommend = fin_lit

# Condition group 3: Advanced learners
else:
    if career_interest == "developer" and learning_style == "practical":
        recommend = web_dev
    elif career_interest == "analyst":
        recommend = data_science
    else:
        recommend = fin_lit

# Output recommendation
print("We recommend the course:", recommend)