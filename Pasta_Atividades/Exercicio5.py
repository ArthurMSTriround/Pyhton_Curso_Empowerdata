#5.1.1 - Dada a lista abaixo, aplique as seguintes operações:
lista = [1, 100, 'Instagram', 'Python', 100, True, 0, False]

#adicione o elemento Empowerdata no final da lista
lista.append("Empowerdata")
print(lista)
#adicione o elemento 149.50 na segunda posição da lista
lista.insert(1, 149.50)
print(lista)

#remova o elemento Instagram da lista
lista.remove('Instagram')
print(lista)

#modifique o elemento False para True
lista[5] = False
print(lista)

#verifique se o elemento de índice 5 é igual ao elemento de índice 7
if lista[5] == lista[7]:
  print("Os elementos são iguais")
else:
  print("Os elementos são diferentes")