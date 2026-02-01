import re
S="Random <tag>first</tag>some text<tag>second</tag>end"
rs=re.findall(r"<tag>.*</tag>",S)
print(rs)