print("\t JOÃO, O PESCADOR")
p=float(input("Qual o peso da pesca total obtido?\nR: "))
if p > 50:
    e= p-50
    m = e*4
else:
    e=0
    m=0

print("Peso: ",p, "kg" "\nExcesso: ", e," kg", "\nMulta: R$ ",f'{m:.2f}')