import random
import string
L1 = []
for i in range(10):
    str = ""
    for j in range(8):
        ch = random.choice(string.ascii_lowercase)
        str+=ch
    print(str)