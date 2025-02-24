#5.2.1 - Dado o dicionário abaixo, aplique as seguintes operações:
dados = {
    'nome': 'Empowerdata',
    'curso': 'Primeiros passos na linguagem Python',
    'modulo': 'Exercícios de fixação',
    'nota obtida': 9.2
}

#imprima qual é o nome do curso
print(dados['curso'])

#altere a nota obtida para 10.0
dados['nota obtida'] = 10.0

print(dados)

#apague o elemento modulo
dados.pop('modulo')
print(dados)

#imprima o nome do curso, com a primeira letra de cada palavra em maiúsculo
print(dados['curso'].title())