'''
Entrada de 3 notas de 0 a 10.
Saída: média aritmética das notas; se a média for
maior ou igual a 6, aprovado; se a média for menor
reprovado.
'''

while True:
  entrada1 = input('Digite o primeiro número inteiro: ')

  if entrada1.isdigit():
    numero1 = int(entrada1)
    break
  else:
    print("O que tu digitou não é um número inteiro.")

while True:
  entrada2 = input('Digite o segundo número inteiro: ')

  if entrada2.isdigit():
    numero2 = int(entrada2)
    break
  else:
    print("O que tu digitou não é um número inteiro.")

while True:
  entrada3 = input('Digite o terceiro número inteiro: ')

  if entrada3.isdigit():
    numero3 = int(entrada3)
    break
  else:
    print("O que tu digitou não é um número inteiro.")

media = (numero1+numero2+numero3)/3
print("A média dos três números digitados é:", media)