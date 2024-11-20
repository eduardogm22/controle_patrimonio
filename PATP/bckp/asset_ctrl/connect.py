# Arquivo para conexão e funções que interagem com o banco de dados
import mysql.connector # type: ignore
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel
from datetime import datetime
import os, json

data_user = ''
data_pass = ''
data_cargo = 15

if os.path.exists('line/dados.json'):
    print("Arquivo JSON existe.")
    v_j = json.load(open("line/dados.json"))
    data_user = v_j["user"]
    data_pass = v_j["password"]
    data_cargo = v_j["cargo"]
    print('Usuário:', data_user, 'Senha:', data_pass, 'Cargo:', data_cargo,'connect')
else:
    print("Arquivo JSON inexistente connect.")



config = {
        'host': 'localhost',
        'database': 'asset_ctrl', 
        'user': 'root',
        'password': ''
        }

        
config_acess = {
        'host': 'localhost',
        'database': 'asset_ctrl',
        'user': 'root',
        'password': ''
        }
 
def criar_conexao():
    return mysql.connector.connect(**config)

def fechar_conexao(con):
    con.close()

def conecta_view_tela(view):
    con = criar_conexao()
    cursor = con.cursor()
    cursor.execute(view)
    dados = cursor.fetchall()
    colunas = [desc[0] for desc in cursor.description]

    modelo = QStandardItemModel(len(dados), len(colunas))
    modelo.setHorizontalHeaderLabels(colunas)
    
    for idx_linha, dados_linha in enumerate(dados):
        for idx_coluna, dados_celula in enumerate(dados_linha):
            dado = QStandardItem(str(dados_celula))
            modelo.setItem(idx_linha, idx_coluna, dado) 

    cursor.close()
    fechar_conexao(con)
        
    return modelo

def conecta_procedure_tela(procedure, parametro):
    con = criar_conexao()
    cursor = con.cursor()
    cursor.callproc(procedure, [parametro])
    
    dados = []
    colunas = []
    
    resultados = cursor.stored_results()
    for resultado in resultados:
        if not colunas:
            colunas = [desc[0] for desc in resultado.description]
        dados.extend(resultado.fetchall())
    
    modelo = QStandardItemModel(len(dados), len(colunas))
    print(colunas)
    modelo.setHorizontalHeaderLabels(colunas)
    
    for idx_linha, dados_linha in enumerate(dados):
        for idx_coluna, dados_celula in enumerate(dados_linha):
            dado = QStandardItem(str(dados_celula))
            modelo.setItem(idx_linha, idx_coluna, dado) 

    cursor.close()
    fechar_conexao(con)
        
    return modelo





# função para registrar (onde ocorreu, tipo de alteração, descrição de alteração, quem fez)
def registrar_log(setor, tipo_modificacao, descricao, id_usuario):
    try:
        con = config_acess
        cursor = con.cursor()

        agora = datetime.now()
        data_modificacao = agora.date()
        hora_modificacao = agora.time()

        query = '''
        INSERT INTO logs (setor, tipo_modificacao, hora_modificacao, data_modificacao, descricao, id_usuario)
        VALUES (%s, %s, %s, %s, %s, %s)
        '''
        valores = (setor, tipo_modificacao, hora_modificacao, data_modificacao, descricao, id_usuario)

        cursor.execute(query, valores)
        con.commit()

        print("Log registrado com sucesso.")
    except Exception as e:
        print(f"Erro ao registrar o log: {e}")
    finally:
        cursor.close()
        con.close()


