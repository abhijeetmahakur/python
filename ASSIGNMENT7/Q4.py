import random
n = 5000
EH = n/10
dict = {i:0 for i in range(0,10)}
print("Before: ", dict)
for i in range(n):
    u = random.randint(0,9)
    dict[u]+=1
#print(dict)
for i in range(0,10):
    hit = dict[i]/EH
    print(f"Element: {i} No of times: {dict[i]} Ratio: {hit}")