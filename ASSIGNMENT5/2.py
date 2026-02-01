try:
    with open("data.txt","w")as f:
        f.write("python is a good programming language")
    with open("data.txt","r")as f:
        data=f.read()
        print(data)
except:
    print("Successfully handle exception")
    print("File not found")