try:
    with open("poem.txt","w")as f:
        f.write("Roses are red,\nViolets are blue,\npython is fun,\nAnd so are you")
    with open("poem.txt","r")as f:
        data=f.read()
        print(data)
except:
    print("Successfully got mypoem printed")
    print("File not found")