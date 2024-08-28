'''
criar um programa que determine a taxa de juros de um empréstimo com base em dois fatores: 
o valor do empréstimo e o histórico de crédito (Bom, Ruim). A taxa é determinada da seguinte forma:

	•	Se o valor do empréstimo for superior a R$ 20.000:
    •   Se o histórico de crédito for “Bom”, a taxa de juros é 5%.
    •	Caso contrário, a taxa de juros é 10%.
	•	Se o valor do empréstimo for R$ 20.000 ou menos:
    •	E se o histórico de crédito for “Bom”, a taxa de juros é 7%.
    •	Caso contrário, a taxa de juros é 12%.
'''
    
emprestimo = float(input("Digite o valor do empréstimo: "))
credito = input("Digite o histórico de crédito (1 - Bom, Outra tecla - Ruim): ")
if emprestimo > 20000:
    if credito == "1":
        taxa = 0.05
    else:
        taxa = 0.10
else:
    if credito == "1":
        taxa = 0.07
    else:
        taxa = 0.12
print(f"A taxa de juros para este cliente é de {taxa * 100}%.")