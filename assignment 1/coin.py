import random

def toss_coin():
    return random.choice(['Heads', 'Tails'])

for _ in range(10):
    print(toss_coin())