a=int(input("Income of the person: "))
if a>100000:
    print("Income is high",a)
elif a>50000 and a<100000:
    print("Income is average", a)
elif a>10000 and a<50000:
    print("Income is less",a)
else:
    print("Poor Income",a)
