print("\t\tAprovação através da média")
m=float(input("Digite sua média: "))
if m>=0 and m<=10:
    if m>=5:
        print ("Aprovado com a média: ", m)
    elif m >=3:
        print ("Exame com a média: ", m)
    else:
        print ("Reprovado com a média: ", m)
else:
 print("Média inválida.")

