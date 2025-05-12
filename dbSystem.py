import sqlite3
from typing import List
from typesSystem import Tarefa
import logging

DB_FILE = 'tarefas.db'

def criar_tabela() -> None:
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tarefas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                descricao TEXT NOT NULL,
                concluida BOOLEAN NOT NULL CHECK (concluida IN (0, 1))
            )
        ''')

def carregar_tarefas() -> List[Tarefa]:
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id, titulo, descricao, concluida FROM tarefas')
        return cursor.fetchall()

def adicionar_tarefaDB(titulo: str, descricao: str) -> None:
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO tarefas (titulo, descricao, concluida) VALUES (?, ?, ?)',
            (titulo, descricao, False)
        )

def marcar_tarefa_concluidaDB(id_tarefa: int) -> None:
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        # Corrigido "concluída" para "concluida" (sem acento)
        cursor.execute('UPDATE tarefas SET concluida = ? WHERE id = ?', (True, id_tarefa))

def remover_tarefaDB(id_tarefa: int) -> None:
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM tarefas WHERE id = ?', (id_tarefa,))
