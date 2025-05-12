from dbSystem import carregar_tarefas, adicionar_tarefaDB, marcar_tarefa_concluidaDB, remover_tarefaDB
from typesSystem import Tarefa
from typing import List
import logging

# Função para listar todas as tarefas
def listar_tarefas() -> None:
    tarefas: List[Tarefa] = carregar_tarefas()
    if not tarefas:
        print("\nNenhuma tarefa adicionada até o momento.\n\n")
        return
    
    print("\n---------------------------")

    for id_, titulo, descricao, concluida in tarefas:
        status = "Concluída" if concluida else "Pendente"
        print(f"{id_}. {titulo} - {descricao} ({status})")
        logging.warning("Listou todas as tarefas.")
    print("---------------------------\n\n")

# Função para adicionar uma nova tarefa
def adicionar_tarefa() -> None:
    titulo: str = input("Digite o título da tarefa: ")
    if not titulo.strip():
        logging.warning("Tentativa de adicionar tarefa sem título.")
        print("ATENÇÃO! Título não pode estar vazio.\n")
        return
    
    descricao: str = input("Digite a descrição da tarefa: ")
    if not descricao.strip():
        logging.warning("Tentativa de adicionar descrição vazia.")
        print("ATENÇAO! Descrição não pode estar vazia.\n")
        return
    
    adicionar_tarefaDB(titulo, descricao)
    print("Tarefa adicionada com sucesso!")
    logging.info(f"Tarefa adicionada: {titulo}")
    

# Função para marcar uma tarefa como concluída
def marcar_tarefa_concluida() -> None:
    listar_tarefas()
    
    try:
        id_tarefa: int = int(input("Digite o número da tarefa que deseja marcar como concluída: "))
    except ValueError:
        print("Por favor, insira um número válido.")
        logging.warning("Inseriu valores que não são do tipo INT ao tentar buscar uma tarefa.")
        return
    marcar_tarefa_concluidaDB(id_tarefa)
    print("Tarefa marcada como concluída!")
    logging.warning(f"Tarefa do ID {id_tarefa} marcada como concluída.")

# Função para remover uma tarefa
def remover_tarefa() -> None:
    listar_tarefas()
    try:
        id_tarefa: int = int(input("Digite o número da tarefa que deseja remover: "))
    except ValueError:
        print("ATENÇÃO: ID inválido.")
        return
    
    tarefas = carregar_tarefas()
    tarefa = next((t for t in tarefas if t[0] == id_tarefa), None)

    if not tarefa:
        print("Tarefa não encontrada.")
        logging.warning(f"Tentativa de remover tarefa inexistente: ID {id_tarefa}")
        return


    titulo = tarefa[1]
    descricao = tarefa[2]

    remover_tarefaDB(id_tarefa)
    print("Tarefa removida com sucesso!")
    logging.warning(f"Removeu a tarefa {id_tarefa} - {titulo}: {descricao}")