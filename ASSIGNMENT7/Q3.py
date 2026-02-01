import random
n = 10000
sum_dict = {i:0 for i in range(2,13)}
print("Before throwing dice: ",sum_dict)
for i in range(n):
    dic1 = random.randint(1,6)
    dic2 = random.randint(1,6)
    total = (dic1 + dic2)
    sum_dict[total]+=1
#print("After throwing dice: ",sum_dict)
for i in range(2,13):
    prob = sum_dict[i]/n
    print(f"Element: {i} No of times: {sum_dict[i]} Probabilty: {prob}")


