import random
num = random.randint(1, 100)
user = int(input("Guess the number: (1-100):"))
count = 1
while (True):
    if num == user:
        print("You guessed it!")
        break
    elif num > user:
        print("TO low!")
        count += 1
        user = int(input("Guess the number: (1-100):"))
    elif num < user:
        print("TO high")
        count += 1
        user = int(input("Guess the number: (1-100):"))
print(f"Total count is : {count}")
