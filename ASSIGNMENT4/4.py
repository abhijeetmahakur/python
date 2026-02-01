import re
n ="i set of 23 owl,999 doves "
rs=re.search(r"\d{2,}",n)
print("Matched:",rs.group())
print("Span:",rs.span())