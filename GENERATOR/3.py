import random
def gen():
    temp=round(random.uniform(20,30),2)
    yield temp
tm=gen()
for i in range(5):
    print(next(tm))
    time.sleep(2)         