scores=[40,50,70,90,67,76]
avg=sum(scores)/len(scores)
mxs=max(scores)
mns=min(scores)
print(f"Average score:{avg}")
print(f"Maximum score:{mxs}")
print(f"Minimum score:{mns}")
avavg=[x for x in scores if x>=avg]
print("Above average score")
print(avavg)
scores.sort(reverse=True)
print("Sorted scores")
print(scores)
scores[-1:-4:-1]=[0,0,0]
print(scores)