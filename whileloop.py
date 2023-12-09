c,b=[int(i) for i in input("Enter the number ").split(",")]
print("Minval: ",c, "Max val:",b)
if c%2!=0: c+=1
while c<b:

     print(c)
     c += 2
