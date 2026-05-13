print("cement=4000,soil=20000,steel bar=15, wire=8000")
tot=0
conti=int(input("enter 1 to continue 0 to exit"))
while conti ==1:
    
    item_price=float(input("enter the price of item"))
    qty=int(input("enter quantity"))
    tot=tot+item_price*qty

    conti=int(input("enter 1 to continue 0 to exit"))
if tot>100000:
    tot=tot*0.95
print("Total bill is",tot)
          
