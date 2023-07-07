lista = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#--------------------------------Letra A
print("a)", lista[1:10],"\n")
#--------------------------------Letra B
print("b)", lista[9:14],"\n")
#print("c)")
#--------------------------------Letra C
 
print("c)",(lista[::2]),"\n")
#--------------------------------Letra D

print("d)",(lista[1::2]),"\n")
#for i in range (1,15):
 #   if i/i == i and i/i == i: 
  #      print("e",lista[i])
#---------------------------------Letra E
print("e)")
print("\t",lista[2::2])
print("\t",lista[3::3])
print("\t",lista[4::4],"\n")
  #-------------------------------Letra F
lista.sort(reverse=True)
print("f)",lista, "\n")
lista.sort()
#---------------------------------Letra G 
x=sum (lista[10:16])
print("g)",x,"\n")
#---------------------------------Letra H
lista.append(16)
print("h)",lista,"\n")
#---------------------------------Letra H
lista1=lista[:]
lista1.remove (16)
lista1.insert(6,16)
print("i)",lista1,"\n")


    