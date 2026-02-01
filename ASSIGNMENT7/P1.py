#Understanding random
"""import random
x = random.random()
print(x)"""

#random numbers from 2 to 10 but only even numbers are generated
'''import random
x = random.randrange(2,10,2)
print(x)'''

#random numbers from 2 to 10 with 10 included
'''import random
x = random.randint(2,10)
print(x)'''

#reverse is also possible
'''import random
x = random.uniform(5,2)
print(x)'''                                            

#randomly choosen from list or tupple
'''import random
x = random.choice([10,12,23,34,45,546])     
print(x)'''

#Using shuffle
'''import random
x = [10,20,30,40,50]
random.shuffle(x)
print(x)'''