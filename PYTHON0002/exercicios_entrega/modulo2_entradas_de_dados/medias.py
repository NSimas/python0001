'''
Exercício 2

entrada:
Digite a primeira nota: 4

Digite a segunda nota: 5

Digite a terceira nota: 6

Digite a quarta nota: 7

saída:
A média aritmética é 5.5
'''
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))

media = nota1 + nota2 + nota3 + nota4 / 4

print(f'A média aritmética é {media}')