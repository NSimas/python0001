'''
Escreva um programa em Python para remover duplicatas de uma lista.
'''
def contador_duplicatas(lista_1):
    from collections import Counter
    contagem_dup = Counter(lista_1)
    duplicatas = {item: count for item, count in contagem_dup.items() if count > 1}
    return duplicatas

def deleta_duplicatas(lista_1):
    lista_limpa = list(set(lista_1))
    return lista_limpa

def menu():
    while True:
        print("\n===== MENU DE DUPLICATAS =====")
        lista_1 = input("Digite os elementos separados por espaço, tecle enter ao terminar: ").split()
        
        print("\nEscolha uma opção:")
        print("1. Contar duplicatas")
        print("2. Deletar duplicatas e mostrar a lista sem duplicatas")
        escolha = input("Digite o número da opção desejada: ")

        try:
            escolha = int(escolha)
            if escolha == 1:
                duplicatas = contador_duplicatas(lista_1)
                if duplicatas:
                    print(f"As duplicatas encontradas foram: {duplicatas}")
                else:
                    print("Não encontramos duplicatas na lista digitada.")
            elif escolha == 2:
                lista_limpa = deleta_duplicatas(lista_1)
                print(f"A lista sem duplicatas é: {lista_limpa}")
            else:
                print("Opção inválida. Por favor, escolha uma opção do menu.")

        except ValueError:
            print("Entrada inválida. Por favor, digite um número para a opção.")

        continuar = input("Deseja voltar ao menu principal? 1 - Para voltar / Outra tecla para sair: ")
        if continuar != '1':
            print("Obrigado por usar o removedor de duplicatas. Até a próxima! =D")
            break

menu()
