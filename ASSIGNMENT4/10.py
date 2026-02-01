import re
def find_repeated_letters(s):
    it=re.finditer(r"(.)\1",s)
    for k in it:
        print(k)
        print(k.group())
        print(k.group(1))
        print(k.span())
    print (it)
s="aa bbb cccc zzzzz"
find_repeated_letters(s)