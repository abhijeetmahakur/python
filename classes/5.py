print("enter the year")
yrs= int(input())
if(yrs%4==0 and yrs%100!=0)or(yrs%400==0):
    print("IT IS A leap year")