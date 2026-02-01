import struct
num=1025
big=struct.pack(">H",num)
lit=struct.pack("<H",num)
print("big=",big)
print("lit=",lit)