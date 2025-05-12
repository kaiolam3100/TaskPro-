from dbSystem import criar_tabela
from viewSystem import adicionar_tarefa, listar_tarefas, marcar_tarefa_concluida, remover_tarefa
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='log_tarefas.log',
    filemode='a'
)

# Função para exibir o menu
def exibir_menu():
    print("\nGerenciador de Tarefas")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Marcar Tarefa como Concluída")
    print("4. Remover Tarefa")
    print("5. Sair")

# Função principal
def main():
    criar_tabela()
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            adicionar_tarefa()
        elif escolha == '2':
            listar_tarefas()
        elif escolha == '3':
            marcar_tarefa_concluida()
        elif escolha == '4':
            remover_tarefa()
        elif escolha == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()