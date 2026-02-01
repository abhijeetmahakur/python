import re

def extract_date_parts(s):
    rs = re.search(r"(\d{2})-(\d{2})-(\d{4})", s)
    print("group()", rs.group())
    print("group(0)", rs.group(0))
    print("group(1)", rs.group(1))
    print("group(2)", rs.group(2))
    print("group(3)", rs.group(3))
    print("span()", rs.span())
    
    return (rs.group(0),rs.group(1),rs.group(2),rs.group(3),rs.group(rs.lastindex))

s = " Date:15-12-2023"
print(extract_date_parts(s))
