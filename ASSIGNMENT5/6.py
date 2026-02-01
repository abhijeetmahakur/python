from datetime import datetime
notes=input("Enter the diary notes:")
try:
    with open("diary.txt","r")as f:
         with open("diary.txt","x")as f1:
             data=f1.read()
             print(data)
except Exception as e:
     with open("diary.txt","w+")as f:
         cd=datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
         f.write(f"Notes:{notes}\n Date{cd}")
         f.seek(0)
         print(f.read())
try:
    with open("diary1.txt","r")as f:
        print(f.read())
except:
    print("File not found.Please check the file name")
             


