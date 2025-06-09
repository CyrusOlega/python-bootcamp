import random
from collections import Counter

random_numbers = [random.randint(0, 1000) for i in range(1000000)]
print(Counter(random_numbers))