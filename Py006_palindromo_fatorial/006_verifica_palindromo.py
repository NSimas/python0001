'''
Verifica e informa se a entrada é, ou não, um
palíndromo.
(Um palíndromo é uma palavra que é lida da mesma 
forma tanto da esquerda para a direita quanto da 
direita para a esquerda.)
'''

while True:
  entrada1 = input('Digite uma palavra para verificar se é um palíndromo ou / para sair: ')

  if (entrada1 == '/'):
    break

  elif entrada1.isalpha():
    palavra1 = entrada1[::-1]

    if (entrada1 == palavra1):
      print('Você digitou um palíndromo, pois ', entrada1, ' invertida é ', palavra1, ' e ambas são iguais! =}')
    else:
      print('Você NÃO digitou um palíndromo, pois ', entrada1, ' invertida é ', palavra1, ' e elas não são iguais! =}')

  else:
    print("O que tu digitou não contém apenas letras.")