# Write a Python function that can accept any number of sales amounts as positional
# arguments (*args) and additional information (such as the name of the salesperson,
# date, and location) as keyword arguments (**kwargs). The function should perform
# the following tasks:
# • Add up all the sales amounts provided through *args.
# • Count and display how many pieces of extra information were provided
# through **kwargs.
# Example Output:
# Total Sales Amount: 12500
# Number of Extra Information Items: 3
# Extra Information Provided:
# Name: John Doe
# Date: 2025-11-01
# Location: Bhubaneswar

def key_fun(*args,**kwargs):
    sum_sales=sum(args)
    extra_info_count=len(kwargs)
    print(f"Total sales amount={sum_sales}")
    print(f"Extra information added={extra_info_count}")
    if extra_info_count>0:
        for key,values in kwargs.items():
            print(f"{key}: {values}")
key_fun(2000,3000,4000,Name='Anup',Date='8/11/2025',Address='Baharagora')