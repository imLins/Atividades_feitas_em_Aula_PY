lista=[]
p=0
for i in range (4):
    lista.append(float(input(f"Digite o {i+1}° número: ")))
    p=p+1
x=sum(lista)
x=x/p
print(lista,"\nMédia: ",x)