import random

rows = int(input("Enter matrix rows: "))
hidden = [random.randint(1, 10) for _ in range(rows)]

for i in range(rows):
    count = 0
    while True:
        guess = int(input(f"Guess row {i+1}: "))
        count += 1
        if guess == hidden[i]:
            print("Correct in", count, "tries")
            break
