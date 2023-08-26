import itertools
import random
import statistics


# Let 1 == ace
deck = list(itertools.product(range(1, 14), [
            'Spade', 'Heart', 'Diamond', 'Club']))

positions = []

for i in range(0, 10000):
    random.shuffle(deck)
    pos = 0
    for j in deck:
        pos += 1
        if j[0] == 1:
            positions.append(pos)
            break

# print(positions)
print(statistics.mean(positions))
print(statistics.median(positions))