ne=0
eo=0
ef=0
#id=int(input("sua idade: "))
#for i in range (1,5,1):
id=int(input("digite sua idade: "))
while (id<=0 or id>=100):
        id=int(input("Reditigite sua idade:"))
if id <16:
        ne=ne+1
elif id >=18 and id <=65:
        eo=eo+1
else:
        ef=ef+1
print(" EF:",ef,"EO",eo,"NE", ne)
        
        