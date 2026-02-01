import random
import string
lets = string.ascii_lowercase
count = {i:0 for i in lets}
#print(count)
for i in range(100):
    ch = random.choice(lets)
    count[ch]+=1
print(count)