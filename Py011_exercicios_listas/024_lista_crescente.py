'''
Escreva um programa em Python para ordenar uma lista em ordem crescente.
'''

def ordenar_lista_crescente():
    while True:
        try:
            entrada = input("Digite uma lista de números inteiros separados por vírgula: ")
            lista = [int(item.strip()) for item in entrada.split(",")]

            if not lista:
                print("ERRO: A lista está vazia.")
                continue

            lista.sort()
            return lista

        except ValueError:
            print("ERRO: Digite apenas números inteiros separados por vírgulas!")

print('----- Vamos pegar uma lista de números e ordenar de forma crescente -----')
print(ordenar_lista_crescente())