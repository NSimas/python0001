'''
Verifica se o número digitado é 
par ou ímpar e informa ao usuário.
'''

while True:
  entrada1 = input('Digite um número inteiro ou / para sair: ')

  if (entrada1 == '/'):
    break

  elif (entrada1 == 0):
    print('Você digitou 0, que não é par nem ímpar.')

  elif entrada1.isdigit():
    numero1 = int(entrada1)

    if (numero1 % 2 == 0):
      print('Você digitou ', numero1, ', que é um número par.')

    else:
      print('Você digitou ', numero1, ', que é um número ímpar.')

  else:
    print("O que tu digitou não é um número inteiro.")