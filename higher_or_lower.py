import random

answer = random.randint(1, 100)
guess = int(input())

while guess != answer:
    if guess > answer:
        print("Lower")
    elif guess < answer:
        print("Higher")
    guess = int(input())

print("Correct")