print ("\t MENU DA CALCULADORA\n 1- SOMA\n 2- MULTIPLICAÇÃO \n 3- SUBTRAÇÃO\n 4- DIVISÃO")
e=int(input("DIGITE A OPÇÃO DO MENU DESEJADA: "))
if e <1 or e >4:
    print("NUMERO DO MENU INVALIDO.")

else:
    n1=float(input("\nDigite o primeiro número para realizar a operação: "))
    n2=float(input("\nDigite o segundo número para realizar a operação: "))
    if e == 1:
        r = n1+n2
        print (n1, "+", n2, "=", f'{r:.2f}')
    elif e == 2:
        r=n1*n2
        print (n1, "x", n2, "=",f'{r:.2f}')
    elif e == 3:
        r = n1 - n2
        print (n1, "-", n2, "=", f'{r:.2f}')
    elif e == 4 and n1 > 0 and n2 > 0:
        r= n1/n2
        print (n1, "/", n2, "=", f'{r:.2f}')
    else:
        print("NAO É POSSIVEL DIVIDIR POR ZERO")

