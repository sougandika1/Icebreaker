d="enter the cahracters"
temp=[]
cnt=[]
'''for  i in range(len(d)):
    result=temp.count(d[i])
    print(d[i],"count is : ",result)
    if result==0:
        temp.append(d[i])
        i += 1

print(temp)
#print(res)'''
for c  in d:
    if c not in temp:
        temp.append(c)
print(''.join(temp))
print("No of charatcers: ",len(d))
