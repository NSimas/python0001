'''
Escreva um programa em Python para verificar se uma string é uma substring de outra string.
'''

def verificar_substring():
    string1 = input("Digite a primeira string, pra verificar se está contida na próxima: ")
    string2 = input("Digite a o texto para verificar se contém a primeira substring: ")
    if string1 in string2:
        print(f"{string1} é uma substring de {string2}.")
    else:
        print(f"{string1} não é uma substring de {string2}.")
        
def menu():
    while True:
        print("\nMenu:")
        print("1. Verificar outra substring")
        print("2. Sair do sistema")
        escolha = input("Escolha uma opção: ")
        if escolha in ["1", "2"]:
            return escolha
        else:
            print("Opção inválida! Digite de novo.")

def main():
    while True:
        verificar_substring()
        escolha = menu()
        if escolha == "2":
            print("Obrigada por usar o sistema, saindo...")
            break

if __name__ == "__main__":
    main()