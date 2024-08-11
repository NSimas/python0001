'''
O usuário deve inserir um número que seja 
inteiro e positivo, então o sistema 
calcula e exibe o fatorial deste número.

(O fatorial de um número é o produto de 
todos os números inteiros positivos de 1 
até o próprio número.)
'''

def calcularFatorial(numero1):
    if numero1 == 0:
        return 1
    else:
        fatorial1 = 1
        for i in range(1, numero1 + 1):
            fatorial1 *= i
        return fatorial1

while True:
  entrada1 = input('Digite um número inteiro positivo ou / para sair: ')

  if (entrada1 == '/'):
    break

  elif entrada1.isdigit():
    numero1 = int(entrada1)

    if (numero1 >= 0):

      resultado = calcularFatorial(numero1)
      print("O fatorial de", entrada1, "é:", resultado)

    else:

      print("Por gentileza, digite um número inteiro positivo.")

  else:
    print("Por gentileza, digite um número inteiro positivo.")