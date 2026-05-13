i=1
lv=0
ov=0
mv=0
while i<=10:
    bill=float(input("Enter bill ?"))
    if bill<1000:
        lv=lv+1
    elif bill>5000:
        ov=ov+1
    else:
        mv=mv+1
    i=i+1
print("defect-lower value",lv)
print("defect-ower value",ov)
print("medium value",mv)
