n= int(input("Enter the number"))
primflag=True;
for r in range(2,n-1):

    if n%r==0:
       primflag=False;

if (primflag): print("Prime number")
else:
    print("not prime number", n)


""" 
   if(primflag):7
   
       print("Number is prime:", n)
else:
        print("not prime number", n)
 """
