import re

def verify_passwd(ps):
    r1 = re.search(r"^[a-zA-Z0-9@#$%^&*!]{8,}$", ps)   # min length 8
    r2 = re.search(r"\d+", ps)                         # contains digit
    r3 = re.search(r"[a-zA-Z]+", ps)                   # contains letter
    r4 = re.search(r"[!@#$%^&*]+", ps)                 # contains special char
    return bool(r1 and r2 and r3 and r4)

psw = "Abc@12377"

if verify_passwd(psw):
    print(f"{psw} is a valid password")
else:
    print(f"{psw} is not a valid password")
