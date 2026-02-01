a=[[1,2],[2,4]]
b=[[2,3],[4,5]]
c=[]
c=[[sum(a[i][k]*b[k][j]
        for k in range(len(b)))
        for j in range(len(b[0]))]
        for i in range (len(a))]
print("Matrix1")
for i in range(len(a)):
    for j in range(len(a)):
        print(a[i][j],end=" ")
    print()    
print("Matrix2")
for i in range(len(b)):
    for j in range(len(b)):
        print(b[i][j],end=" ")
    print()
print("Result Matrix")
for i in range(len(c)):
    for j in range(len(c)):
        print(c[i][j],end=" ")
        print()