def isprime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
def isodd(n):
    if n%2!=0:
        return True
    else:
        return False
data={
    "A":[2,3,7,5,8,9],
    "B":[2,4,5,7,8,9,11,],
    "C":[4,8,6,9,11]
    "D":[1,2,3,4,5]

}
res={}
for k,v in data.items():
    if isinstanse(v,list):
        s=0
        for i in data[k]:
            if isprime(i):
                s=s+i
    res[k]
    if isinstanse(v,tuple):
        p=1
        for i in data[k]:
            if isprime(i):
                p=p*i
    

