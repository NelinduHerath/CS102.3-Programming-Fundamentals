count=1
low=0
med=0
high=0
tot=0
while count<=10:
    deposit=float(input("Enter deposit -"))
    if deposit<5000:
        low=low+1
    elif deposit<=20000:
        med=med+1
    else:
        high=high+1
    tot=tot+deposit
    count=count+1
avg=tot/10

print("number of low deposits",low)
print("number of medium deposits",med)
print("number of high deposits",high)
print("average deposit of the day",avg)
