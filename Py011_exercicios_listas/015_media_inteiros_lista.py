'''
Escreva um programa em Python para encontrar a média de todos os elementos em uma lista.
'''

def menu():
    while True:
        print("\n===== Média de Elementos de nossa Lista =====")
        lista_1 = input("Digite os elementos pra lista separados por espaço, números inteiros: ").split()
        
        try:
            lista_1 = [int(i) for i in lista_1]
            print(f"A média dos elementos da lista é {sum(lista_1)/len(lista_1)}.")
        
        except ValueError:
            print("Erro: Todos os elementos da lista devem ser números inteiros.")
            continue
        
        continuar = input("Deseja voltar ao menu principal? 1 - Para Menu / Outra tecla para sair: ")
        if continuar != '1':
            print("Obrigado por usar o Média de Elementos em uma Lista. Até a próxima!!! =D")
            break
        
menu()