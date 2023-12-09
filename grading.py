
m,p,c=[int(i) for i in input("Enter 3 subject marks:").split()]

if m>34 and p>34 and c>34:
    print("pass")
    avg=(m+p+c)/3
    print("Average of MArks:",avg)
    if avg >= 69:
        print("Grade A")
    if avg >= 59 and avg < 69: print("Grade B")
    if avg < 59: print("Grade C")

else:
    print("Failed")


#elif avg<=59:print("Grade C")
