import sqlite3

#-----------------------BANCO DE DADOS---------------------- 

def criar_tabelas():
    conn = sqlite3.connect('loja.db')
    cursor = conn.cursor()
    
    # Tabela Cliente
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Cliente (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE,
            telefone TEXT,
            endereco TEXT
        )
    ''')
    
    # Tabela Produto
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Produto (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT,
            preco REAL NOT NULL,
            estoque INTEGER NOT NULL
        )
    ''')
    
    # Tabela Pedido
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
    
    # Tabela ItemPedido
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
    
    conn.commit()
    conn.close()

def get_connection():
    return sqlite3.connect('loja.db')

#--------------------CRUD----------------------

#--------crud do cliente

class CRUDCliente:
    @staticmethod
    def criar_cliente(nome, email, telefone, endereco):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('''
                INSERT INTO Cliente (nome, email, telefone, endereco)
                VALUES (?, ?, ?, ?)
            ''', (nome, email, telefone, endereco))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        finally:
            conn.close()
    
    @staticmethod
    def listar_clientes():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Cliente')
        clientes = cursor.fetchall()
        conn.close()
        return clientes
    
    @staticmethod
    def buscar_cliente(id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Cliente WHERE id = ?', (id,))
        cliente = cursor.fetchone()
        conn.close()
        return cliente
    
    @staticmethod
    def atualizar_cliente(id, nome, email, telefone, endereco):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE Cliente 
            SET nome = ?, email = ?, telefone = ?, endereco = ?
            WHERE id = ?
        ''', (nome, email, telefone, endereco, id))
        conn.commit()
        conn.close()
        return cursor.rowcount > 0
    
    @staticmethod
    def deletar_cliente(id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Cliente WHERE id = ?', (id,))
        conn.commit()
        conn.close()
        return cursor.rowcount > 0
    
#--------crud do produto


class CRUDProduto:
    @staticmethod
    def criar_produto(nome, descricao, preco, estoque):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Produto (nome, descricao, preco, estoque)
            VALUES (?, ?, ?, ?)
        ''', (nome, descricao, preco, estoque))
        conn.commit()
        conn.close()
        return True
    
    @staticmethod
    def listar_produtos():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Produto')
        produtos = cursor.fetchall()
        conn.close()
        return produtos
    
    @staticmethod
    def buscar_produto(id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Produto WHERE id = ?', (id,))
        produto = cursor.fetchone()
        conn.close()
        return produto
    
    @staticmethod
    def atualizar_produto(id, nome, descricao, preco, estoque):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE Produto 
            SET nome = ?, descricao = ?, preco = ?, estoque = ?
            WHERE id = ?
        ''', (nome, descricao, preco, estoque, id))
        conn.commit()
        conn.close()
        return cursor.rowcount > 0
    
    @staticmethod
    def atualizar_estoque(id, nova_quantidade):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE Produto SET estoque = ? WHERE id = ?
        ''', (nova_quantidade, id))
        conn.commit()
        conn.close()
        return cursor.rowcount > 0
    
    @staticmethod
    def deletar_produto(id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Produto WHERE id = ?', (id,))
        conn.commit()
        conn.close()
        return cursor.rowcount > 0
    
#--------crud do pedidod e dos items do pedido

from datetime import datetime

class CRUDPedido:
    @staticmethod
    def criar_pedido(cliente_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Pedido (cliente_id) VALUES (?)
        ''', (cliente_id,))
        pedido_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return pedido_id
    
    @staticmethod
    def adicionar_item_pedido(pedido_id, produto_id, quantidade):
        conn = get_connection()
        cursor = conn.cursor()
        
        # Buscar preço do produto
        cursor.execute('SELECT preco, estoque FROM Produto WHERE id = ?', (produto_id,))
        produto = cursor.fetchone()
        
        if not produto:
            conn.close()
            return False, "Produto não encontrado"
        
        preco_unitario, estoque_atual = produto
        
        if estoque_atual < quantidade:
            conn.close()
            return False, "Estoque insuficiente"
        
        # Inserir item no pedido
        cursor.execute('''
            INSERT INTO ItemPedido (pedido_id, produto_id, quantidade, preco_unitario)
            VALUES (?, ?, ?, ?)
        ''', (pedido_id, produto_id, quantidade, preco_unitario))
        
        # Atualizar estoque
        novo_estoque = estoque_atual - quantidade
        cursor.execute('UPDATE Produto SET estoque = ? WHERE id = ?', (novo_estoque, produto_id))
        
        # Atualizar total do pedido
        cursor.execute('''
            UPDATE Pedido SET total = (
                SELECT SUM(subtotal) FROM ItemPedido WHERE pedido_id = ?
            ) WHERE id = ?
        ''', (pedido_id, pedido_id))
        
        conn.commit()
        conn.close()
        return True, "Item adicionado com sucesso"
    
    @staticmethod
    def listar_pedidos():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT p.*, c.nome as cliente_nome 
            FROM Pedido p 
            JOIN Cliente c ON p.cliente_id = c.id
        ''')
        pedidos = cursor.fetchall()
        conn.close()
        return pedidos
    
    @staticmethod
    def buscar_pedido(id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT p.*, c.nome as cliente_nome 
            FROM Pedido p 
            JOIN Cliente c ON p.cliente_id = c.id 
            WHERE p.id = ?
        ''', (id,))
        pedido = cursor.fetchone()
        
        # Buscar itens do pedido
        cursor.execute('''
            SELECT ip.*, pr.nome as produto_nome 
            FROM ItemPedido ip 
            JOIN Produto pr ON ip.produto_id = pr.id 
            WHERE ip.pedido_id = ?
        ''', (id,))
        itens = cursor.fetchall()
        
        conn.close()
        return pedido, itens
    
    @staticmethod
    def atualizar_status_pedido(id, novo_status):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE Pedido SET status = ? WHERE id = ?', (novo_status, id))
        conn.commit()
        conn.close()
        return cursor.rowcount > 0
    
    @staticmethod
    def deletar_pedido(id):
        conn = get_connection()
        cursor = conn.cursor()
        
        # Primeiro, restaurar estoque dos produtos
        cursor.execute('''
            SELECT produto_id, quantidade FROM ItemPedido WHERE pedido_id = ?
        ''', (id,))
        itens = cursor.fetchall()
        
        for produto_id, quantidade in itens:
            cursor.execute('SELECT estoque FROM Produto WHERE id = ?', (produto_id,))
            estoque_atual = cursor.fetchone()[0]
            novo_estoque = estoque_atual + quantidade
            cursor.execute('UPDATE Produto SET estoque = ? WHERE id = ?', (novo_estoque, produto_id))
        
        # Deletar itens do pedido
        cursor.execute('DELETE FROM ItemPedido WHERE pedido_id = ?', (id,))
        
        # Deletar pedido
        cursor.execute('DELETE FROM Pedido WHERE id = ?', (id,))
        
        conn.commit()
        conn.close()
        return cursor.rowcount > 0
    
#------------------INTERFACE---------------



class SistemaLoja:
    def __init__(self):
        criar_tabelas()
        self.clientes = CRUDCliente()
        self.produtos = CRUDProduto()
        self.pedidos = CRUDPedido()
    
#--------Principal 

    def menu_principal(self):
        while True:
            print("\n" + "="*50)
            print("SISTEMA DE LOJA - CRUD COMPLETO")
            print("="*50)
            print("1. Gerenciar Clientes")
            print("2. Gerenciar Produtos")
            print("3. Gerenciar Pedidos")
            print("4. Sair")
            
            opcao = input("\nEscolha uma opção: ")
            
            if opcao == '1':
                self.menu_clientes()
            elif opcao == '2':
                self.menu_produtos()
            elif opcao == '3':
                self.menu_pedidos()
            elif opcao == '4':
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida!")
    

    #--------Cliente

    def menu_clientes(self):
        while True:
            print("\n" + "-"*30)
            print("GERENCIAR CLIENTES")
            print("-"*30)
            print("1. Listar Clientes")
            print("2. Cadastrar Cliente")
            print("3. Buscar Cliente")
            print("4. Atualizar Cliente")
            print("5. Deletar Cliente")
            print("6. Voltar")
            
            opcao = input("\nEscolha uma opção: ")
            
            if opcao == '1':
                self.listar_clientes()
            elif opcao == '2':
                self.cadastrar_cliente()
            elif opcao == '3':
                self.buscar_cliente()
            elif opcao == '4':
                self.atualizar_cliente()
            elif opcao == '5':
                self.deletar_cliente()
            elif opcao == '6':
                break
            else:
                print("Opção inválida!")
    
    def listar_clientes(self):
        print("\n--- LISTA DE CLIENTES ---")
        clientes = self.clientes.listar_clientes()
        if not clientes:
            print("Nenhum cliente cadastrado.")
            return
        
        for cliente in clientes:
            print(f"ID: {cliente[0]} | Nome: {cliente[1]} | Email: {cliente[2]} | Telefone: {cliente[3]}")
    
    def cadastrar_cliente(self):
        print("\n--- CADASTRAR CLIENTE ---")
        nome = input("Nome: ")
        email = input("Email: ")
        telefone = input("Telefone: ")
        endereco = input("Endereço: ")
        
        if self.clientes.criar_cliente(nome, email, telefone, endereco):
            print("Cliente cadastrado com sucesso!")
        else:
            print("Erro ao cadastrar cliente. Email já existe?")
    
    def buscar_cliente(self):
        try:
            id = int(input("ID do cliente: "))
            cliente = self.clientes.buscar_cliente(id)
            if cliente:
                print(f"\nID: {cliente[0]}")
                print(f"Nome: {cliente[1]}")
                print(f"Email: {cliente[2]}")
                print(f"Telefone: {cliente[3]}")
                print(f"Endereço: {cliente[4]}")
            else:
                print("Cliente não encontrado!")
        except ValueError:
            print("ID deve ser um número!")
    
    def atualizar_cliente(self):
        try:
            id = int(input("ID do cliente para atualizar: "))
            cliente = self.clientes.buscar_cliente(id)
            if not cliente:
                print("Cliente não encontrado!")
                return
            
            print("Deixe em branco para manter o valor atual:")
            nome = input(f"Nome [{cliente[1]}]: ") or cliente[1]
            email = input(f"Email [{cliente[2]}]: ") or cliente[2]
            telefone = input(f"Telefone [{cliente[3]}]: ") or cliente[3]
            endereco = input(f"Endereço [{cliente[4]}]: ") or cliente[4]
            
            if self.clientes.atualizar_cliente(id, nome, email, telefone, endereco):
                print("Cliente atualizado com sucesso!")
            else:
                print("Erro ao atualizar cliente!")
        except ValueError:
            print("ID deve ser um número!")
    
    def deletar_cliente(self):
        try:
            id = int(input("ID do cliente para deletar: "))
            if self.clientes.deletar_cliente(id):
                print("Cliente deletado com sucesso!")
            else:
                print("Cliente não encontrado!")
        except ValueError:
            print("ID deve ser um número!")
    
    #--------Produto

    def menu_produtos(self):
        while True:
            print("\n" + "-"*30)
            print("GERENCIAR PRODUTOS")
            print("-"*30)
            print("1. Listar Produtos")
            print("2. Cadastrar Produto")
            print("3. Buscar Produto")
            print("4. Atualizar Produto")
            print("5. Deletar Produto")
            print("6. Voltar")
            
            opcao = input("\nEscolha uma opção: ")
            
            if opcao == '1':
                self.listar_produtos()
            elif opcao == '2':
                self.cadastrar_produto()
            elif opcao == '3':
                self.buscar_produto()
            elif opcao == '4':
                self.atualizar_produto()
            elif opcao == '5':
                self.deletar_produto()
            elif opcao == '6':
                break
            else:
                print("Opção inválida!")
    
    def listar_produtos(self):
        print("\n--- LISTA DE PRODUTOS ---")
        produtos = self.produtos.listar_produtos()
        if not produtos:
            print("Nenhum produto cadastrado.")
            return
        
        for produto in produtos:
            print(f"ID: {produto[0]} | Nome: {produto[1]} | Preço: R${produto[3]:.2f} | Estoque: {produto[4]}")
    
    def cadastrar_produto(self):
        print("\n--- CADASTRAR PRODUTO ---")
        nome = input("Nome: ")
        descricao = input("Descrição: ")
        try:
            preco = float(input("Preço: R$ "))
            estoque = int(input("Estoque: "))
            
            if self.produtos.criar_produto(nome, descricao, preco, estoque):
                print("Produto cadastrado com sucesso!")
            else:
                print("Erro ao cadastrar produto!")
        except ValueError:
            print("Preço deve ser um número e estoque deve ser inteiro!")
    
    #--------Pedido
    
    def menu_pedidos(self):
        while True:
            print("\n" + "-"*30)
            print("GERENCIAR PEDIDOS")
            print("-"*30)
            print("1. Listar Pedidos")
            print("2. Criar Pedido")
            print("3. Buscar Pedido")
            print("4. Adicionar Item ao Pedido")
            print("5. Atualizar Status")
            print("6. Deletar Pedido")
            print("7. Voltar")
            
            opcao = input("\nEscolha uma opção: ")
            
            if opcao == '1':
                self.listar_pedidos()
            elif opcao == '2':
                self.criar_pedido()
            elif opcao == '3':
                self.buscar_pedido()
            elif opcao == '4':
                self.adicionar_item_pedido()
            elif opcao == '5':
                self.atualizar_status_pedido()
            elif opcao == '6':
                self.deletar_pedido()
            elif opcao == '7':
                break
            else:
                print("Opção inválida!")
    
    def listar_pedidos(self):
        print("\n--- LISTA DE PEDIDOS ---")
        pedidos = self.pedidos.listar_pedidos()
        if not pedidos:
            print("Nenhum pedido cadastrado.")
            return
        
        for pedido in pedidos:
            print(f"ID: {pedido[0]} | Cliente: {pedido[5]} | Data: {pedido[2]} | Status: {pedido[3]} | Total: R${pedido[4]:.2f}")
    
    def criar_pedido(self):
        print("\n--- CRIAR PEDIDO ---")
        self.listar_clientes()
        try:
            cliente_id = int(input("\nID do cliente: "))
            pedido_id = self.pedidos.criar_pedido(cliente_id)
            print(f"Pedido criado com ID: {pedido_id}")
        except ValueError:
            print("ID deve ser um número!")
    
    def adicionar_item_pedido(self):
        print("\n--- ADICIONAR ITEM AO PEDIDO ---")
        try:
            pedido_id = int(input("ID do pedido: "))
            self.listar_produtos()
            produto_id = int(input("ID do produto: "))
            quantidade = int(input("Quantidade: "))
            
            sucesso, mensagem = self.pedidos.adicionar_item_pedido(pedido_id, produto_id, quantidade)
            print(mensagem)
        except ValueError:
            print("IDs e quantidade devem ser números!")
    

if __name__ == "__main__":
    sistema = SistemaLoja()
    sistema.menu_principal()