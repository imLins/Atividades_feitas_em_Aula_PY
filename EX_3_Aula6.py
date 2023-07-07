print ("\t\tClasse eleitoral")
id=int(input("Digite sua idade: "))
if id<16:
    print("Não eleitor.")
elif id>=16 and id<18 or id>65:
      print ("Facultativo.")
elif id>=18 and id<=65:
      print ("Obrigatório.")
else: 
    print ("Idade inválida.") 