# Project: Building a self grading quiz

# The topic is open
# 7 questions minimum
# multiple choice (A,B,C,D)
# You need to ask for the user name,
# store it and use it to address the user.
# keep track of correct answers and incorrect answers
# Provide the user with their final score.

# Theme: Star Wars Movies

# 1. Why is Obi Wan better than Anakin?
print("1. Why is Obi Wan better than Anakin?")

# Right answer to question 1: C
correctAnswer1 = "C"

# A) He was his master
print("A) He was his master")
# B) Becuase he had more experience
print("B) Becuase he had more experience")
# C) Because he had the higher ground.
print("C) Because he had the higher ground")

userAnswer1 = input("What is your choice?...")

userAnswer2 = input("What is your choice?...")

if userAnswer2 == "B" or "D":
    print("Thats correct")
else:
    print("thats wrong")