#  Write a Python program that checks voting eligibility using filter() and dictionary comprehension. The program should perform the following tasks:
# a) Use filter() to extract eligible voters (age ≥ 18 and nationality = ”Indian”).
# b) Count and display the total number of eligible voters.
# c) Build a dictionary using dictionary comprehension in the format
# {’Eligible’:[...], ’Not Eligible’:[...]}.
# Input: A list of tuples containing voter information — name, age,
# and nationality. (e.g., [(”Amit”,22,”Indian”), (”John”,30,”USA”),
# (”Neha”,17,”Indian”), (”Ravi”,19,”Indian”)])
# Output: Eligible: [”Amit”, ”Ravi”]
# Count: 2
# {’Eligible’: [’Amit’, ’Ravi’], ’Not Eligible’: [’John’, ’Neha’]}

l=[('Amit',22,'Indian'), ('John',30,'USA'),('Neha',17,'Indian'), ('Ravi',19,'Indian')]
def key_fun(x):
    if x[1]>=18 and ('Indian' in x[2]):
         return(x)
selected=list(filter(key_fun,l))
eligible_name=[x[0] for x in selected]
print('Eligible voters are:',eligible_name)
print('Number of eligible voters =',len(eligible_name))
not_eligible=[x[0] for x in l if x[0]  not in eligible_name]
req={'Eligible':[],'Not Eligible':[]}
for i in l:
    if i in selected:
        req['Eligible']=eligible_name
    else:
        req['Not Eligible']=not_eligible
print(req)