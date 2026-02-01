from functools import reduced
li = [10, 20, 30, 40, 50]
sum = reduced(lambda x,y: x +y, li)
print(sum)
