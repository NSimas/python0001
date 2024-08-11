# CRUD melhorado.

def adicionarTarefa(tarefas, tarefa_id, tarefa_texto):
    tarefas[tarefa_id] = {'descricao': tarefa_texto, 'concluida': False}
    print("Tarefa adicionada com sucesso!")

def listarTarefas(tarefas):
    if not tarefas:
        print("Não encontramos tarefas salvas.")
    else:
        print("Tarefas:")
        for tarefa_id, tarefa in tarefas.items():
            status = "CONCLUIDA" if tarefa['concluida'] else "PENDEDNTE"
            print(f"{tarefa_id}. {tarefa['descricao']} - {status}")

def concluirTarefa(tarefas, tarefa_id):
    if tarefa_id in tarefas:
        tarefas[tarefa_id]['concluida'] = True
        print("Tarefa marcada como concluída! =}")
    else:
        print("ID de tarefa inválido!")

def deletarTarefa(tarefas, tarefa_id):
    if tarefa_id in tarefas:
        del tarefas[tarefa_id]
        print(f"A tarefa foi excluída com sucesso!!")
    else:
        print("ID de tarefa inválido!")

def menu():
    tarefas = {}
    next_id = 1
    
    while True:
        print("\n===== Gerenciador de Tarefas portátil II =====")
        print("1. Adicionar uma nova tarefa.")
        print("2. Listar todas as tarefas existentes.")
        print("3. Marcar uma tarefa existente como concluída.")
        print("4. Excluir uma tarefa existente.")
        print("5. Encerrar/Sair do programa")

        escolha = input("Digite o número da opção: ")

        match escolha:
            case "1":
                tarefa_texto = input("Digite a nova tarefa: ")
                adicionarTarefa(tarefas, next_id, tarefa_texto)
                next_id += 1
            case "2":
                listarTarefas(tarefas)
            case "3":
                listarTarefas(tarefas)
                if not tarefas:
                    print("Não há tarefas para marcar como concluída.")
                else:
                    try:
                        tarefa_id = int(input("Digite o ID da tarefa que deseja marcar como concluída: "))
                        concluirTarefa(tarefas, tarefa_id)
                    except ValueError:
                        print("Por favor, digite um número válido.")
            case "4":
                listarTarefas(tarefas)
                if not tarefas:
                    print("Não há tarefas para excluir.")
                else:
                    try:
                        tarefa_id = int(input("Digite o ID da tarefa que deseja remover: "))
                        deletarTarefa(tarefas, tarefa_id)
                    except ValueError:
                        print("Por favor, digite um número válido.")
            case "5":
                print("Obrigado por usar o Gerenciador de Tarefas. Até mais!")
                break
            case _:
                print("Opção inválida. Por favor, escolha uma opção válida.")

        continuar = input("Deseja voltar ao menu principal? 1 - Para voltar / Outra tecla para sair: ")
        if continuar != '1':
            print("Obrigado por usar o Gerenciador de Tarefas II. Até mais!")
            break

menu()
