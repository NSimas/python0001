'''
Entrada de Dados:

Por favor, entre com o número de segundos que deseja converter: 178615

Saída de Dados:

2 dias, 1 horas, 36 minutos e 55 segundos.
'''

segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dias = segundos // 86400
resto = segundos % 86400

horas = resto // 3600
resto = resto % 3600

minutos = resto // 60
segundos = resto % 60

print(f"{dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos.")