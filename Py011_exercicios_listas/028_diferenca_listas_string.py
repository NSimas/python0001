'''
Escreva um programa em Python para encontrar a diferença entre duas listas.
'''

def ler_lista(mensagem):
    while True:
        try:
            entrada = input(mensagem)
            lista = [item.strip() for item in entrada.split(",")]
            return lista
        except ValueError:
            print("ERRO: Algo deu errado, digite letras, números e caracteres apenas!")

def diferenca_listas():
    lista1 = ler_lista("Digite a primeira lista, os caracteres separados por vírgula: ")
    lista2 = ler_lista("Digite a segunda lista, os caracteres separados por vírgula: ")
    d1 = list(set(lista1) - set(lista2))
    d2 = list(set(lista2) - set(lista1))
    diferenca = list(set(d1 + d2))
    print(f"Diferença entre as listas digitadas: {diferenca}")
    return diferenca

def menu():
    while True:
        print("\nMenu:")
        print("1. Digitar mais listas")
        print("2. Sair do sistema")
        escolha = input("Escolha uma opção: ")
        if escolha in ["1", "2"]:
            return escolha
        else:
            print("Opção inválida! Digite de novo.")
            
def main():
    while True:
        diferenca_listas()
        escolha = menu()
        if escolha == "2":
            print("Obrigada por usar o sistema, saindo...")
            break
        
if __name__ == "__main__":
    main()