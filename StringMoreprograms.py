'''s=input("enter the string:")
print(s[::-1])
j=len(s)-1
result=''
while(j>=0):
   result = result+s[j]
   j-=1
print(result)
if result==s:
   print("palandrome")
else:
   print("not palandrome")'''
'''s='_'.join(['a','b','c'])
print(s)'''
#reverse the string
'''s=input("enter the string:")
print(''.join(reversed(s)))'''
#...........................
# .................
# Reverse the words in a string
'''s="all there words are reversed"
result=s.split()
rever=[]
i=len(result)-1
while i>=0:
    rever.append(result[i])
    i=i-1
print(rever)
output=' '.join(rever)
print("outpu: ",output)
print(result)'''
#reverse the characters in the word
s="How are you"
w=s.split()
print("split: ",w)
wc=len(w)
print("WordCount:",wc)
i=0
result=[]
#result=''
while i<wc :
    each=w[i]
    result.append(each[::-1])
#    result=result+' '+each[::-1]
    i+=1
    print("each word",i,"is: ",each,".rever: ",each[::-1])
print("Reversed string: ",' '.join(result))
#print("Output: ",result)
