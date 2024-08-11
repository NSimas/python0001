'''
Escreva um programa em Python para contar o número de vogais em uma string.
'''
def contar_vogais(frase):
    vogais = 'AEIOU'
    contador_vogais = 0
    for letra in frase:
        if letra.upper() in vogais:
            contador_vogais += 1
    print(f"A frase '{frase}' tem {contador_vogais} vogais.")
    return contador_vogais

def menu():
    while True:
        print("\n===== Contador de Vogais =====")
        frase = input("Digite uma frase e vamos descobrir quantas vogais há nela: ")
        contar_vogais(frase)
        continuar = input("Deseja voltar ao menu principal? 1 - Para Menu / outra tecla para sair: ")
        if continuar != '1':
            print("Obrigado por usar o Contador de Vogais. Até a próxima!!! =D")
            break

menu()