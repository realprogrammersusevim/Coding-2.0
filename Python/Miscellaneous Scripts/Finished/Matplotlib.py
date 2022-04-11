import random
import numpy as np

random_numbers = []

def add_random_number():
    random_number = random.randrange(1, 100, 1)
    random_numbers.append(random_number)

for x in range(0, 10000):
    add_random_number()

median = np.median(random_numbers)
average = np.mean(random_numbers)
standard_deviation = np.std(random_numbers)
variance = np.var(random_numbers)

print(median)
print(average)
print(standard_deviation)
print(variance)
