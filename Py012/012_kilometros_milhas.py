'''
Escreva um programa em Python para converter quilômetros em milhas.
'''

def km_para_milhas(km):
    return km / 1.60934

def milhas_para_km(milhas):
    return milhas * 1.60934

def menu():
    while True:
        print("\n===== Conversor de Kilômetros e Milhas =====")
        print("1. Converter Kilômetros para Milhas.")
        print("2. Converter Milhas para Kilômetros.")
        print("3. Encerrar/Sair do programa")
        
        escolha = input("Digite o número da opção: ")
        
        try:
            escolha = int(escolha)

            if escolha == 1:
                km = float(input("Digite a distância em Kilômetros: "))
                milhas = km_para_milhas(km)
                print(f"{km:.2f} Kilômetros são {milhas:.2f} Milhas.")
                
            elif escolha == 2:
                milhas = float(input("Digite a distância em Milhas: "))
                km = milhas_para_km(milhas)
                print(f"{milhas:.2f} Milhas são {km:.2f} Kilômetros.")
                
            elif escolha == 3:
                print("Obrigado por usar o Conversor de Kilômetros e Milhas. Até a próxima!!! =D")
                break
            
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")

            continuar = input("Deseja voltar ao menu principal? 1 - Para Menu / outra tecla para sair: ").strip().lower()
            if continuar != '1':
                print("Obrigado por usar o Conversor de Kilômetros e Milhas. Até a próxima!!! =D")
                break

        except ValueError:
            print("Digite um número válido. Use ponto como separador decimal.")
        continuar = input("Deseja voltar ao menu principal? 1 - Para Menu / outra tecla para sair: ").strip().lower()
        if continuar != '1':
            print("Obrigado por usar o Conversor de Kilômetros e Milhas. Até a próxima!!! =D")
            break

menu()