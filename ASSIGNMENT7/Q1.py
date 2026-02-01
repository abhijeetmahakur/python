import random
l1 = []
for i in range(1000):
    x = random.choice(["H","T"])
    l1.append(x)
H = l1.count("H")
T = l1.count("T")
print("Total no of head: ",H)
print("Total no of tail: ",T)
print("Probability of Getting Head: ",H/1000)
print("Probability of Getting Tail: ",T/1000)      