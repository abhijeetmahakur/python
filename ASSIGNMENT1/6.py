def encryption(st):
    st = st[::-1]  # reverse the string
    li = list(st)
    for i in range(0, len(li) - 1, 2):
        li[i], li[i+1] = li[i+1], li[i]  # swap pairs
    return ''.join(li)

def decryption(st):
    li = list(st)
    for i in range(0, len(li) - 1, 2):
        li[i], li[i+1] = li[i+1], li[i]  # swap back
    st = ''.join(li)
    return st[::-1]  # reverse again to get original

st = input("Enter the String: ")
enstr = encryption(st)
destr = decryption(enstr)

print("Original String:", st)
print("Encrypted String:", enstr)
print("Decrypted String:", destr)
