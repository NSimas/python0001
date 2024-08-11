'''
Escreva um programa em Python para contar o número de ocorrências de um elemento em uma lista.
'''

def menu():
    while True:
        print("\n===== CONTADOR DE OCORRÊNCIAS =====")
        lista_1 = input("Digite os elementos separados por espaço, tecle enter ao terminar: ").split()
        
        try:
            lista_1 = [str(i) for i in lista_1]
            elemento = input("Digite o elemento que deseja contar as ocorrências: ")
            print(f"O elemento '{elemento}' aparece {lista_1.count(elemento)} vezes na lista digitada.")
        
        except ValueError:
            print("ERRO: Algo saiu errado!")
            continue
        
        continuar = input("Deseja voltar ao menu principal? 1 - Para voltar / Outra tecla para sair: ")
        if continuar != '1':
            print("Obrigado por usar o contador de ocorrências. Até a próxima! =D")
            break
        
menu()