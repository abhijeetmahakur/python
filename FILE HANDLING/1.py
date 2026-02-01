f=open("C:/Users/ITER/Desktop/Abhijeet06/FILE HANDLING/ab.txt","r")
data=f.read()
print(data)
f.close()

with open("C:/Users/ITER/Desktop/Abhijeet06/FILE HANDLING/ab.txt","w")as f:
    f.write("hello world")
    
    
    
with open("C:/Users/ITER/Desktop/Abhijeet06/FILE HANDLING/abc.txt","x")as f:
    f.write("hello world")
    
    
with open("C:/Users/ITER/Desktop/Abhijeet06/FILE HANDLING/abc.txt","a")as f:
    f.write("Abhijeet is a bad boy")