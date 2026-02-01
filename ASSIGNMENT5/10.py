import pickle
dict1={"Alice":(20,"A"),"BOB":(19,"B"),"Charlie":(21,"A")}
with open("file1.text","wb")as f:
    pickle.dump(dict1,f)
with open("file1.text","rb")as f:
    d1=pickle.load(f)
    print(d1)