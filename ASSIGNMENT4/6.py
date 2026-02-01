import re
def check(s):
    pattern=r"^[a-z]+[0-9]+$"
    return bool(re.match(pattern,s))
str=["abc123","a1b2","ABC123"]
for s in str:
    if check(s):
        print(f"{s}")
        
        