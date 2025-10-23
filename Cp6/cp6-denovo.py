

import sqlite3


def criar_tabela():
    connect = sqlite3.connect('loja.db')
    cursor = connect.cursor()

    #tabela Cliente
    cursor.execute('''CREATE TABLE IF NOT EXISTS Cliente (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE,
            telefone TEXT,
            endereco TEXT
        )
    ''')
    #tabela Produto
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Produto (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT,
            preco REAL NOT NULL,
            estoque INTEGER NOT NULL
        )
    ''')
    #tabela Pedido
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Pedido (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id INTEGER NOT NULL,
            data_pedido DATE DEFAULT (date('now')),
            status TEXT DEFAULT 'Pendente',
            total REAL DEFAULT 0,
            FOREIGN KEY (cliente_id) REFERENCES Cliente (id)
        )
    ''')

    #tabela ItemPedido
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ItemPedido (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pedido_id INTEGER NOT NULL,
            produto_id INTEGER NOT NULL,
            quantidade INTEGER NOT NULL,
            preco_unitario REAL NOT NULL,
            subtotal REAL GENERATED ALWAYS AS (quantidade * preco_unitario) VIRTUAL,
            FOREIGN KEY (pedido_id) REFERENCES Pedido (id),
            FOREIGN KEY (produto_id) REFERENCES Produto (id)
        )
    ''')

    connect.commit()
    connect.close()

def conection():
    return sqlite3.connect('loja.db')

#CRUD!!!!!!!!!!!!!!!!!!
class CRUDcliente:
    @staticmethod
    def criarCliente(nome,email,telefone,endereco):
        return
