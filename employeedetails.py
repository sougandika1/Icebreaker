sno= int(input("enter the no of employees : "))

empdata={}
for n in range(sno):
    sname = input("enter the emp name: ")
    sal = int(input("Enater emp sal:"))
    empdata[sname]=sal
while True:
      name= input("enter the emp name: ")
      salary=empdata.get(name,-1)
      if salary>0:
        print("salary of ",name, "is :",salary )
      else:
        print("Employee does not eixst:", name)
      choice=input("Do you want ot know th sal of another emploeye [Yes/No]")
      if choice=='No':
              break

   # print(n,"salary is :",s)


