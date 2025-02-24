""" 
Neste desafio, vamos aumentar um pouquinho o nível de complexidade do exercício. Vamos utilizar os conceitos que praticamos acima, junto com as estruturas de repetição e condicionais para resolver o problema.
**Problema**
A lista abaixo contém as seguintes informações de pessoas que pretendem dirigir:

- `nome`: nome da pessoa
- `carteira`: **`True`** para as que possuem, **`False`** para as que não possuem
- `idade`:a idade da pessoa

Precisamos percorrer toda a lista e verificar se a pessoa pode ou não dirigir. Só podem dirigir as que possuem carteira **E** que a idade é maior ou igual a 18 anos.

- para as pessoas que podem dirigir, imprima a frase: **`nome pode dirigir.`**
- para as que não podem, imprima: **`nome não pode dirigir!`** 
"""

pessoas = [ ('Vinicius', True, 21), ('Gabriel', False, 25), ('Ana', True, 20), ('Victor', True, 30), ('Lucas', False, 15) ]

for nome, carteira, idade in pessoas:
    if carteira and idade>=18:
        print(f'{nome} pode dirigir.')
    else:
        print(f'{nome} não pode dirigir!')