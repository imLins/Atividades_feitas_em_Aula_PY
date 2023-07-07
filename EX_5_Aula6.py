print("\n-----------------Nota Fiscal-----------------\n \t Hotel Sr. Café")
ta= str(input("\nQual o tipo do apartamento a qual você de hospedou?\nR: ")).upper()
if ta =="A" or ta == "B" or ta == "C" or ta == "D":
    nome= str(input("Qual o seu nome?\nR: "))
    d= int(input("Quantos dias você se hospedou?\nR: "))
    ci=float(input("Qual foi custo interno?\nR: "))
    if ta =="A":
        vd=150
    elif ta=="B":
        vd= 100
    elif ta =="C":
        vd = 75
    else:
        vd = 50
        
    dia=d*vd
    sub=ci+dia
    ts=sub*.1
    total= sub+ts
    print("\nNome: ",nome ,"\nTipo do apartamento: ", ta, "\nDias hospedado: ",d, "\nValor unitário da diária: R$ ",vd, "\nValor total da Diaria: R$",dia)
    print("Consumo Interno Utilizado: R$",ci,"\nSubTotal: R$",sub,"\nTaxa de Serviço: R$ ", ts,"\nTotal: R$",f'{total:.2f}')
    
else:
    print("\t\nTIPO DE APARTAMENTO INCORRETO...")
    
