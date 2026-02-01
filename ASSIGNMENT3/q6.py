# Write a Python generator function called filter high sales that takes a list of daily
# sales amounts and a threshold value.
# • The function should yield only those sales amounts that are greater than or
# equal to the given threshold.
# • Demonstrate this generator by providing it with a list of sales and printing all
# high sales (e.g., sales above $500).
# Example Output:
# Daily Sales: [250, 800, 450, 1200, 600]
# Threshold: 500
# High Sales:
# 800
# 1200
# 600

def daily_sales(sales,threshold):
    for ch in sales:
        if ch>=threshold:
            yield ch
sales=input('Input sales seoperated by spaces')
sales_present=list(map(int,sales.split()))
threshold=int(input('Enter threshold value'))
for i in daily_sales(sales_present,threshold):
    print(i, end=' ')