make=[]
model=[]
eng=[]
count=0
while count<4:
    m= str(input("enter brand name"))
    make.append(m)
    mod=m= str(input("enter model name"))
    model.append(mod)
    en=float(input("enter engine cpty"))
    eng.append(en)
    count=count+1
print(make)
print(model)
print(eng)
