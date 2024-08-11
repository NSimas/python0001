'''
Escreva um programa em Python para encontrar o menor elemento em uma lista.
'''

def menu():
    while True:
        print("\n===== MENOR ELEMENTO =====")
        lista_1 = input("Digite os elementos separados por espaço, números inteiros: ").split()
        
        try:
            lista_1 = [int(i) for i in lista_1]
            print(f"O menor elemento digitado foi {min(lista_1)}.")
        
        except ValueError:
            print("ERRO: Todos os elementos da lista precisam ser números inteiros!")
            continue
        
        continuar = input("Deseja voltar ao menu principal? 1 - Para voltar / Outra tecla para sair: ")
        if continuar != '1':
            print("Obrigado por usar o localizador de menor número da lista. Até a próxima!!! =D")
            break

menu()