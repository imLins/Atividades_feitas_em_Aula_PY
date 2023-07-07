print("Soma das médias aritméticas")
soma=0
n=int(input("Digite o número de alunos: "))
for i in range (1,n,1):
    nt1=float(input("Digite a primeira nota: "))
    nt2=float(input("Digite a segunda nota: "))
    media=(nt1+nt2)/2
    print("A sua média é de: ",media)
    soma=soma+media
mediasala=soma/n
print("A média da sala é: ", mediasala)
#the same resolution exercise 9 or 8