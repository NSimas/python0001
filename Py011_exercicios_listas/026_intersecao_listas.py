'''
Escreva um programa em Python para encontrar a interseção de duas listas.
'''
 
def ler_lista(mensagem):
    while True:
        try:
            entrada = input(mensagem)
            lista = [int(item.strip()) for item in entrada.split(",")]
            return lista
        except ValueError:
            print("ERRO: Digite apenas números inteiros separados por vírgula!")
            
def intersecao_listas():
    lista1 = ler_lista("Digite a primeira lista de números inteiros separados por vírgula: ")
    lista2 = ler_lista("Digite a segunda lista de números inteiros separados por vírgula: ")
    intersecao = list(set(lista1) & set(lista2))
    print(f"Interseção das listas digitadas: {intersecao}")
    return intersecao

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
        intersecao_listas()
        escolha = menu()
        if escolha == "2":
            print("Obrigada por usar o sistema, saindo...")
            break

if __name__ == "__main__":
    main()