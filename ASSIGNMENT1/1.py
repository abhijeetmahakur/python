def generate_bill(item,price,quantity=1,discount=0,tax_rate=0.5):
    sub_total=price*quantity
    disprice=sub_total*(1-discount)
    tax_price=disprice*tax_rate
    totalamt=disprice+tax_price
    print("Bill Summary")
    print("Item:",item)
    print("Quantity:",quantity)
    print("Price:",price)
    print("Discount:",discount)
    print("Tax:",tax_price)
    print("total amount:",totalamt)
generate_bill("Laptop",50000)
generate_bill("Laptop",50000,2)
generate_bill("Laptop",50000,2,.1)
generate_bill("Laptop",50000,taxrate=.07, discount=.01,quantity=3)