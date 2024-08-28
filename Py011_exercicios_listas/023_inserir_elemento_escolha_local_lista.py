'''
Escreva um programa em Python para inserir um elemento em uma posição específica em uma lista.
'''

def inserir_elemento():
    try:
        entrada = input("Digite uma lista de números inteiros separados por vírgula: ")
        lista = [int(item.strip()) for item in entrada.split(",")]

        if len(lista) == 0:
            return "ERRO: A lista está vazia."

        elemento = int(input("Digite o número novo que deseja inserir: "))
        posicao = int(input("Digite a posição da lista em que deseja inserir o número novo digitado: "))

        lista.insert(posicao, elemento)
        return lista

    except ValueError:
        return "ERRO: Digite apenas números inteiros!"
    
print(inserir_elemento())