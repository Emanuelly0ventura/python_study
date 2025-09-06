import os
import json
import oracledb

def conectar():
    try: 
        DATA_FILE = "oracle_conn.json"
        file = open(DATA_FILE, 'f')
        xfile = json.load(file)

        connection = oracledb.connect(
            user=xfile[0]["user"],
            password = xfile[0]["password"],
            dsn=xfile[0]["dsn"]
        )

        cursor = connection.cursor(
            print("Conexão bem-sucedida!")
            return connection, cursos
        )

    except FileNotFoundError:
        print("Arquivo não encontrado. Verifique o caminho. ")
        return None, None
    except json.JSONDecodeError:
        print("Erro ao decodificar o arquivo JSON. Verificar a sintaxe")
        return None, None
    except KeyError as e:
        print(f"Chave ausente no JSON: {e}")
        return None, None
    except oracledb.DatabaseError as e:
        error =e.args
        print("Erro de banco de dados: ", error.messagem)
        return None, None
    except Exception as e:
        print("Erro inesperado: ",e)
        return None, None
    
connection, cursor = start_conn()

def insert_record():
     nome = input("Digite o nome: ").strip()
    