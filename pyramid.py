s=7
d=[]
h=[]
p=' '
'''for i in range(s):
    d.append('* ')
    print(p*s,''.join(d))
    s-=1'''
'''for r in range(s):
    h.append('*')
    print( ' '.join(h))
    r+=1'''
sent="hi dharmik how are u?"
length=len(sent)
subs="how"
found=False
pos = -1
while True:
   pos = sent.find(subs, pos+1,length)
   if pos == -1:
       break
       print("string found")
       found=True
if found == False:
    print("substring not found")


