s=input("enter the word:")
v={'a','e','i','o','u'}
results={}
for i in s:
    if i in v:
        results[i]=results.get(i,0)+1
        print(results[i],"-",results.get(i,0)+1)
for k,v1 in sorted(results.items()):
    print(k, "is presentsowgandhika ", v1, "times")





