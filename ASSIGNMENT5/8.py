vlen="python is a good"
fixedlen=vlen.ljust(20)
print(vlen)
print(len(vlen))
print(len(fixedlen))
with open("zz.txt","wb")as f:
    f.write(fixedlen.encode())
with open("zz.txt","rb")as f:
   print(f.read().decode())