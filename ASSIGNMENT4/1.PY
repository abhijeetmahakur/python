import re

def filter_emails(l1):
    pattern = r"^[a-zA-Z0-9][a-zA-Z0-9._]*@[a-zA-Z]+\.[a-zA-Z]{2,3}$"
    valid = []
    for s1 in l1:
        if re.findall(pattern, s1):
            valid.append(s1)
    return valid

em = ["student123@gmail.com", "teacher.name@soa.edu", "abc.xyz12@abc", "bad@ln.com"]
li = filter_emails(em)

if len(li) == 0:
    print("There is no valid email")
else:
    print(li)
