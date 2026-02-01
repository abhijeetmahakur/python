import string
sen=input("Enter the sentence:" )
sen=sen.translate(str.maketrans("","",string.punctuation))
sen.sen.lower()
freq={}
cleansen=sen.spilit()
for i in cleansen:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)
