"""
7-Funções
7.1 - Desafio 🔥🔥🔥

a) Crie uma função que receba 3 argumentos:

- nome
- carteira (True ou False)
- idade

e verifique se a pessoa pode ou não dirigir. 
- caso possa dirigir, a função deve imprimir a frase **`nome pode dirigir.`**
- caso negativo, deve imprimir **`nome não pode dirigir!`**

b) **reescreva a solução do último desafio utilizando a função que você criou!**
"""

import pandas as pd
dados = {
    'nome': ['Arthur', 'Marcos', 'Rafael', 'Leonardo', 'Lucyan'],
    'Carteira': [True, True, True, False, True],
    'idade': [26, 27, 27, 29 ,28]
}
df =pd.DataFrame(dados)
print(df)

Dados2 = [ ('Arthur', True, 26), ('Marcos', True, 27), ('Rafael', True, 27), ('Lucyan', True, 28), ('Leonardo', False, 29) ]
for nome,carteira,idade in Dados2:
    if carteira and idade >= 18:
        print(f'{nome} pode dirigir!')
    else:
        print(f'{nome} não pode dirigir!')