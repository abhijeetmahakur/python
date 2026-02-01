import string
sen=input("Enter the sentence")
sep=input("Enter the seperator")
sen=sen.translate(str.maketrans("","",string.punchutation))
sen=sen.lower().strip()
words=sen.split()
words.sort(reverse=True)
sen=sep.join(words)
print(sen)