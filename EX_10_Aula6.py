print("------------------ Declaração de imposto -------------------")
n=input("Nome: ")
cpf=input("CPF: ")
ra=float(input("Renda Anual: "))
nd=int(input("Número de dependentes: "))
if ra>0 and nd>=0:
    dd= 110*nd
    rl= ra-dd
    if rl<=800:
        al=1
        i= rl*al
        a=0
    elif rl<=4000:
        a=0.025
    elif rl<=9000:
        a=0.05
    else:
        a=0.1
    i= rl*a
    print("\n\n ------------------ Declaração de imposto ------------------\n\n")
    print ("Nome: ",n)
    print ("CPF: ",cpf)
    print ("Renda Líquida: ",rl)
    print ("Imposto: ",i)
    ax= a*100
    print ("Alíquota: ",ax,"%")
else:
    print("Não é capaz de realizar o Cálculo com os dados digitados...")