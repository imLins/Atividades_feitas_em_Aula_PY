lista=[]
p=0
for i in range (6):
    lista.append(int(input(f"Digite o {i+1}° número: ")))
for i in (lista):
    print("Posição",p,"º:", i)
    p=p+1
        