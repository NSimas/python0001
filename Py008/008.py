'''
CRUD basicão com listas.
'''

def adicionarTarefa(tarefas, tarefa):
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

def listarTarefas(tarefas):
    if not tarefas:
        print("Não há tarefas salvas para visualizar.")
    else:
        print("Tarefas:")
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa}")

def concluirTarefa(tarefas, indice):
    if indice >= 1 and indice <= len(tarefas):
        tarefas.pop(indice - 1)
        print("Tarefa marcada como concluída!")
    else:
        print("Índice de tarefa inválido!")

def deletarTarefa(tarefas, indice):
    if indice >= 1 and indice <= len(tarefas):
        tarefas.pop(indice - 1)
        print("Tarefa excluída com sucesso!")
    else:
        print("Índice de tarefa inválido!")

#função do menú principal
def menu():
    tarefas = []

    while True:
        print("\n===== Gerenciador de Tarefas portátil =====")
        print("1. Adicionar uma nova tarefa.")
        print("2. Listar todas as tarefas existentes.")
        print("3. Marcar uma tarefa existente como concluída.")
        print("4. Excluir uma tarefa existente.")
        print("5. Encerrar/Sair do programa")

        escolha = input("Digite o número da opção: ")

        match escolha:
            case "1":
                tarefa = input("Digite a nova tarefa: ")
                adicionarTarefa(tarefas, tarefa)
            case "2":
                listarTarefas(tarefas)
            case "3":
                listarTarefas(tarefas)
                indice = int(input("Digite o número da tarefa que deseja marcar como concluída: "))
                concluirTarefa(tarefas, indice)
            case "4":
                listarTarefas(tarefas)
                indice = int(input("Digite o número da tarefa que deseja remover: "))
                deletarTarefa(tarefas, indice)
            case "5":
                print("Obrigado por usar o Gerenciador de Tarefas. Até mais!")
                break
            case _:
                print("Opção inválida. Por favor, escolha uma opção válida.")

# deixando a função menú como inicial a ser executada 
# quando o o script é executado diretamente.

# se usar o script como módulo secundário, o mesmo 
# precisará de adaptações para executar, se usar 
# assim não roda.
if __name__ == "__main__":
    menu()