def gen():
    for i in range(1,11):
        yield i
k=gen()
for i in k:
    print(i)