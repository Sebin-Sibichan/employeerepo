prodname=input("Enter the product name")
price=input("Enter the cost price")
GST=10
priceval=int(price) #explicit type conversion
amt=priceval*GST/100 + priceval
print("The price of",prodname, "is", amt)