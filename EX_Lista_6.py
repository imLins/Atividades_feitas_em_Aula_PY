listaA=[]
listaB=[]
x=int(input("Digite um valor para comparar a tabela A e B: "))
for i in range(15):
    a=int(input(f"Insira o {i+1}ºNúmero da lista A --> "))
    if a>x:
        listaA.append(a) #So numero comaprado for menor que o numero que for
        listaB.append(a)
    else:
        listaA.append(a)
print("Lista A: ",listaA,"\n Lista B: ",listaB)
       