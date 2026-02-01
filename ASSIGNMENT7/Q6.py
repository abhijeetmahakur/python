import random
n = 2000
dict = {i: 0 for i in range(1, 7)}
print("Before:", dict)
for i in range(n):
    u = random.randint(1, 6)
    dict[u] += 1
for i in range(1, 7):
    prob = dict[i] / n
    print(f"Segment: {i} Count: {dict[i]} Probability: {prob}")
highest = max(dict, key=dict.get)
lowest = min(dict, key=dict.get)
print("Highest segment:", highest, "Count:", dict[highest])
print("Lowest segment:", lowest, "Count:", dict[lowest])
