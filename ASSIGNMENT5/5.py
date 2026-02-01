with open("abc.text","rb")as f:
    print("file_pointer_position=",f.tell())
    print(f.read(11))
    print("file_pointer_position=",f.tell())
    f.seek(0)
    print("file_pointer_position=",f.tell())
    print(f.read())
    f.seek(-5,2)
    print(f.read())                                                         