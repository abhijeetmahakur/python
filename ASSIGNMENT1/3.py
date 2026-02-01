month=input("Enter the month:")
monthkeys={'jan':31,'mar':31,'apr':30, 'may':31,'jun':30,'jul':31,'aug':31,'sep':30,'oct':31,'nov':30,'dec':31}
month_name=input("Enter the month name")
month_name=month_name.lower()[0:3]
if (month_name=='feb'):
    year=int(input("Enter the year"))
    if year%400 or year%100==0 and year%4==0:
        print(f"the no of days in{month_name}",29)
    else: 
        print(f"the no of days in{month_name}",28)
else:
    print(f"the no of days in{month_name} is {monthkeys[month_name]}")
         