print ("Cálculo de peso ideal")
h=float(input("Qual sua altura? \nR:"))
if h>1 and h<3:
    s= input("Qual seu sexo biológico?\n F (feminino) \n M (masculino)\nR:").upper()
    if s=='F' or s=='M':
        if s=='F':
            pi=(62.1*h)-44.7
        else:
            pi=(72.7*h)-58
        print ("O seu peso ideal é: ", f'{pi:.2f}')
    else:
        print("Sexo inválido.")
else:
    print("Altura inválida.")
        
    