print("\t\tJogo da adivinhação ;)")
n1=int(input("Jogador 1, digite um número de 1 a 10: "))
while n1<1 or n1>10:
    n1=0
    n1=int(input("Jogador 1, somente digite um número de 1 a 10 "))
n2=int(input("Jogador 2, tente adivinhar o número digitado pelo Jogador 1:"))
t=1
while n2<1 or n2>10:
    n2=0
    n2=int(input("Jogador 2, digite um número entre 1 e 10:"))
while n2!=n1:
    n2=int(input("Jogador 2, número incorreto. Tente novamente:"))
    while n2<1 or n2>10:
        n2=0
        n2=int(input("Jogador 2, digite um número entre 1 e 10:"))
    #n2=int(input("Jogador 2, tente adivinhar o número digitado pelo Jogador 1:"))
    t=t+1
print ("Você acertou!\nCom o número de",t,"tentativas.")
