lista=[]
for i in range (5):
    x=float(input(f"Digite o {i+1}° número: "))
    if x<0:
        x=0
        lista.append(x)
    else:
        lista.append(x)
print(lista)