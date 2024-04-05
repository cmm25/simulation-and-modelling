import random

def toss_coin():
    return random.choice(['Heads', 'Tails'])

for i in range(10):
    result = toss_coin()
    print(f"Toss {i+1}: {result}")