par=input("Enter the paragraph:")
#print(par)
par=par.title()
par=''.join(par.spilit())
vowelcount={}
for i in par:
    if i.upper()not in vowelcount:
        vowelcount[i.upper()]=1
    else:
        vowelcoun