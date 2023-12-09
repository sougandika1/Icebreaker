''' # Assert Example
i=int(input("enter the value>10: "))
assert i>10,"Wrong number"
print("input number is",i) '''

# example to remove duplicates from list
'''list=[1,2,2,3,3,4,5,1]
list1=[]
for each_value in list:
    if each_value not in list1:
        list1.append(each_value)
        print(list1)'''
list=[10,20,30,10,40,20]
s=set(list)
print(s)

