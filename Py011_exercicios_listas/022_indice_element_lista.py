'''
Escreva um programa em Python para encontrar o índice de um elemento em uma lista.
'''

def indice_elemento():
    try:
        entrada = input("Digite uma lista de números inteiros separados por vírgula: ")
        lista = [int(item.strip()) for item in entrada.split(",")]

        if len(lista) == 0:
            return "ERRO: A lista está vazia."

        elemento = int(input("Digite o número que deseja encontrar o índice: "))

        if elemento not in lista:
            return "ERRO: O número não está na lista."
        else:
            print(f"O índice do número {elemento} na lista é: ", end="")

        return lista.index(elemento)

    except ValueError:
        return "ERRO: Digite apenas números inteiros!"