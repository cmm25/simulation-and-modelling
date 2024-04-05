import random
from collections import Counter

# Function to simulate rolling a dice based on a random number between 0 and 1
def roll_dice():
    rand_num = random.random()  # Generates a random number between 0 and 1
    if rand_num < 1/6:
        return 1
    elif rand_num < 2/6:
        return 2
    elif rand_num < 3/6:
        return 3
    elif rand_num < 4/6:
        return 4
    elif rand_num < 5/6:
        return 5
    else:
        return 6

# Simulate rolling the dice 1000 times
rolls = [roll_dice() for _ in range(1000)]

# Count the frequency of each face using Counter
frequency = Counter(rolls)

# Calculate the percentage occurrence of each face
total_rolls = sum(frequency.values())
percentage = {face: (count / total_rolls) * 100 for face, count in frequency.items()}

# Print the table
print("Face\tFrequency\tPercentage")
for face in range(1, 7):
    print(f"{face}\t{frequency[face]}\t\t{percentage[face]:.2f}%")
