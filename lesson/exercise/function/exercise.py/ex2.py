def get_percentage_score(num_questions, num_correct):
    return (num_correct / num_questions) * 100


# We want to use this function to calculate 
# the percentage score of a test with 
# 19 correct answers out of 20 questions.

score = get_percentage_score(20, 19)
print(score)
