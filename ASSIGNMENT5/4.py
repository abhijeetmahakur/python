count_lines=0
count_words=0
count_lets=0
with open ("abc.text","w")as f:
    f.write("python is great.\nIts make coding simple.")
with open("abc.text","r")as f:
    for line in f:
        count_lines=count_lines+1
        count_words=count_words+len(line.split())
        count_lets=count_lets+len(line)
        print(line)
print("No of lines are:",count_lines) 
print("No of words are:",count_words)        
print("No of letters are:",count_lets)               