import re

def check_word(word):
    # starts with c, then vowel, then consonant
    pattern = r"^c[aeiou][b-df-hj-np-tv-z]$"
    return bool(re.match(pattern, word))

print(check_word("cat")) 
print(check_word("cit"))  
print(check_word("cot"))  
print(check_word("cut"))  
print(check_word("caa")) 
print(check_word("sgh"))  
