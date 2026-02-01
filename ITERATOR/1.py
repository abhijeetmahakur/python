list=[20,30,40,50,60]
"""for i in list:
   print(i)
it=iter(list)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))"""

it=iter(list)
while True:
    try:
        print(next(it))
    except:
        break