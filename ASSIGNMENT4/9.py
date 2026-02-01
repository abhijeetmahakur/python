import re
def check(s):
    rs=re.search(r"([A-Z]).*\d",s)
    print(rs.group())
    print(rs.group(1))
    print(rs.span())
    return rs
s="a B blah 1"
print(check(s))