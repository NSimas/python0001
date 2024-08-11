
def segundo_maior():
    try:
        entrada = input("Digite uma lista de (2 ou mais) números inteiros separados por vírgula: ")
        
        lista = [int(x.strip()) for x in entrada.split(",")]

        if len(lista) == 0:
            return "ERRO: A lista está vazia."

        lista_1 = list(set(lista))

        if len(lista_1) < 2:
            return "ERRO: A lista precisa de pelo menos 2 número diferentes!"

        lista_1.sort(reverse=True)
        return lista_1[1]

    except ValueError:
        return "ERRO: Digite apenas números inteiros!"

print(segundo_maior())
