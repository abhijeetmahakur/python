import struct
l=[20,30,40,50,60]
with open("bin1.txt","wb")as f:
    for i in l:
        f.write(struct.pack("i",i))
z=[]      
with open("bin1.txt","rb")as f:
    while True:
        r=f.read(4)
        if r:
            k=struct.unpack("i",r)
            z.append(k)
        else:
            break
print(z)