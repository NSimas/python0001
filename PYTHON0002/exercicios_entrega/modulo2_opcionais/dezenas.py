'''
Exemplo 1:

Entrada de Dados:

Digite um número inteiro: 78615

Saída de Dados:

O dígito das dezenas é 1

Exemplo 2:

Entrada de Dados:

Digite um número inteiro: 2

Saída de Dados:

O dígito das dezenas é 0
'''

inteiro = input("Digite um número inteiro: ")

digitoDezena = int(inteiro) // 10 % 10

print("O dígito das dezenas é", digitoDezena)