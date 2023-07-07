print("Comparativo de crescimento de duas cidades...")
npa=int(input("Digite o número da populaçãoda primeira cidade: "))
pca=float(input("Digite a porcentagem anual do crescimento da população A: "))
npb=int(input("Digite o número da populaçãoda segunda cidade: "))
pcb=float(input("Digite a porcentagem anual do crescimento da população B: "))
CAa=(pca/100)
CAb=(pcb/100)       #Crescimento anual A 
x=0
y=0
z=0
anos=0
st=0
if (npa>npb):    #Define os valores das variaves para realizar o calculo se a Numero de População
    x=npa        # da cidade A for maior que o Nupero de População da cidade B
    y=npb
    z=CAb
else:            #Caso nao for, npb sera maior que npa
    x=npb
    y=npa
    z=CAa
while (st<=x): #Calculo
    st=z*y+y
    anos=anos+1
print("Quantidade de anos necessários: ", anos)

