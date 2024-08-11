
def celsius_para_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def menu():
    while True:
        print("\n===== Conversor de Temperaturas =====")
        print("1. Converter Celsius para Fahrenheit.")
        print("2. Converter Fahrenheit para Celsius.")
        print("3. Encerrar/Sair do programa")
        
        escolha = input("Digite o número da opção: ")
        
        try:
            escolha = float(escolha)

            while True:
                match escolha:
                    case 1:
                        celsius = float(input("Digite a temperatura em Celsius: "))
                        fahrenheit = celsius_para_fahrenheit(celsius)
                        print(f"{celsius:.2f}°C é igual a {fahrenheit:.2f}°F.")
                        break

                    case 2:
                        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
                        celsius = fahrenheit_para_celsius(fahrenheit)
                        print(f"{fahrenheit:.2f}°F é igual a {celsius:.2f}°C.")
                        break

                    case 3:
                        print("Obrigado por usar o Conversor de Temperaturas. Até mais! =D")
                        exit()
            
        except ValueError:
            print("Digite um número válido. Use ponto como separador decimal.")
            continue
        
menu()