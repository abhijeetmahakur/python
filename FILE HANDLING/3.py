with open("asd.txt","w+")as f:
    f.write("Abhijeet \n")
    f.write("this is apython program \n")
    f.seek(0)
    data=f.read()
    print(data)