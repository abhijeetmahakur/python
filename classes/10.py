m1=float(input("enter mark1"))
m2=float(input("enter mark2"))
m3=float(input("enter mark3"))
m4=float(input("enter mark4"))
m5=float(input("enter mark5"))
totalmarks=m1+m2+m3+m4+m5
avg=totalmarks/5
if avg>90:
    print("0 grade")
elif avg>80 and avg<=90:
 print("A grade")
elif avg>70 and avg<=80:
 print("B grade")
elif avg>60 and avg<=70:
 print("C grade")
elif avg>50 and avg<=60:
 print("d grade")
else:
  print("f")


# NESTED IF
m1=float(input("enter mark1"))
m2=float(input("enter mark2"))
m3=float(input("enter mark3"))
m4=float(input("enter mark4"))
m5=float(input("enter mark5"))
totalmarks=m1+m2+m3+m4+m5
avg=totalmarks/5
if avg>90:
  print("0 grade")
else:
  if avg>80 and avg<=90:
    print("A grade")
  else:
    if avg>70 and avg<=60:
      print("B grade")
      if avg>60 and avg<=50:
        print("C grade")
      else:
        print("Fail")
    