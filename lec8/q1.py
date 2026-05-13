i=1
lw=0
ow=0
ac=0
while i<=10:
    w=float(input("Enter weight ?"))
    if w<99.5:
        lw=lw+1
    elif w>100.5:
        ow=ow+1
    else:
        ac=ac+1
    i=i+1
print("defect-lower weight",lw)
print("defect-ower weight",ow)
print("accepted",ac)
