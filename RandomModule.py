import random

print(random.randint(1, 10))  # this includes 10

# choice picks random value from list of values
greetings = ['Hello', 'Hi', 'Hey', 'Hola']
value = random.choice(greetings)
print(value, 'Harsh!')

# 10 random results

colors = ['Red', 'Black', 'Green']

results = random.choices(colors, k=10)
print(results)

# shuffle
deck = list(range(1, 53))
random.shuffle(deck)
print(deck)