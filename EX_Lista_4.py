lista=[]
#p=0
for i in range (5):
    lista.append(int(input(f"Digite o {i+1}° número: ")))
ma=max(lista)
mi=min(lista)
print("Maior número: ",ma,"\nMenor número: ",mi)