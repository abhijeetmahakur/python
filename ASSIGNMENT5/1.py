names=["alice", "bob","eva", "charlie", "david "]
with open("C:/Users/ITER/Desktop/Abhijeet06/ASSIGNMENT5/student.txt","w")as f:
    for i in names:
        f.write(i+"\n")
with open("C:/Users/ITER/Desktop/Abhijeet06/ASSIGNMENT5/student.txt","r")as f1:
    data=f1.read()
    print(data)