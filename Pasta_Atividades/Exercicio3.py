#3.1Verifique se 10 é maior ou igual a 15

numero1 = int(10)
numero2 = int(15)
if numero1>=numero2:
  print(f'{numero1} é maior que número {numero2}')
else:
  print(f'{numero1} é menor que número {numero2}')
  
#3.2 - Verifique se a string Python é igual à string python
nome = str("Python")
nome2 = str("python")
if nome == nome2:
  print(f"{nome} é igual a {nome2}")
else:
  print(f"{nome} é diferente de {nome2}")

#3.3 - Verifique se 100 é menor que 59 E se 200 é maior ou igual a 159
numero3 = int(100)
numero4 = int(59)
numero5 = int(200)
numero6= int(159)

if numero3 < numero4:
  print(f'{numero3} é menor que {numero4}')
else:
  print(f'{numero3} é maior que {numero4}')

if numero5 >= numero6:
  print(f'{numero5} é maior ou igual a {numero6}')
else:
  print(f'{numero5} é menor que {numero6}')
  
#3.4 - Verifique se 100 é maior que 48 OU a string Python é igual à string python
x = 100
y = 48
nome = str("Python")
nome2 = str("python")

if x > y:
  print(f'{x} é maior que {y}')
else:
  print(f'{x} é menor que {y}')

if nome == nome2:
  print(f"{nome} é igual a {nome2}")
else:
  print(f"{nome} é diferente de {nome2}")

#Faça a negação da expressão 10 > 3
a = int(10)
b = int(3)

if a > b:
  print(f'{a} é maior que {b}')
else:
  print(f'{a} é menor que {b}')
  
not a > b
