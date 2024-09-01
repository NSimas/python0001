'''
Escreva um programa em Python para substituir um caractere específico em uma string por outro caractere.
'''

def troca_char(string, char, new_char):
    new_string = ""
    for i in string:
        if i == char:
            new_string += new_char
        else:
            new_string += i
    return new_string

def main():
    while True:
        string = input("Digite uma frase/palavra/algo para depois substituir um caractere: ")
        char = input("Digite um caractere para ser substituído: ")
        if char not in string:
            print("Erro: O caractere não foi encontrado na string.")
            choice = input("Deseja tentar outro caractere? 1 - Sair | outro para tentar novamente: ").lower()
            if choice == 'n':
                print("Saindo...")
                break
        else:
            new_char = input("Digite um novo caractere para substituir o anterior: ")
            print(f"O resultado é: " + troca_char(string, char, new_char))
            break

if __name__ == "__main__":
    main()