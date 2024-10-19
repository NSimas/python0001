'''
entrada:
Digite o nome do cliente: Fulano de Tal
Digite o dia de vencimento: 9
Digite o mês de vencimento: Janeiro
Digite o valor da fatura: 350,00

saída:
Olá, Fulano de Tal
A sua fatura com vencimento em 9 de Janeiro no valor de R$ 350,00 está fechada.
'''

nome = input('Digite o nome do cliente: ')
dtVencimento = int(input('Digite o dia de vencimento: '))
mesVencimento = input('Digite o mês de vencimento: ')
valorFatura = input('Digite o valor da fatura: ')

print(f'Olá, {nome}')
print(f'A sua fatura com vencimento em {dtVencimento} de {mesVencimento} no valor de R$ {valorFatura} está fechada.')