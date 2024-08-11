'''
Escreva um programa em Python para encontrar a soma de todos os elementos em uma lista.
'''

def menu():
    while True:
        print("\n===== Soma de Elementos de nossa Lista =====")
        lista_1 = input("Digite os elementos da lista separados por espaço: ").split()
        
        try:
            lista_1 = [int(i) for i in lista_1]
            print(f"A soma dos elementos da lista é {sum(lista_1)}.")
        
        except ValueError:
            print("Erro: Todos os elementos da lista devem ser números inteiros. Tente novamente.")
            continue
        
        continuar = input("Deseja voltar ao menu principal? 1 - Para Menu / outra tecla para sair: ")
        if continuar != '1':
            print("Obrigado por usar o Soma de Elementos em uma Lista. Até a próxima!!! =D")
            break

menu()