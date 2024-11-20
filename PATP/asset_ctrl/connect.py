# Arquivo para conexão e funções que interagem com o banco de dados
import mysql.connector # type: ignore
from PyQt5.QtGui import QStandardItemModel, QStandardItem
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
        'database': 'cadastro', 
        'user': 'root',
        'password': ''
        }

        
config_acess = {
        'host': 'localhost',
        'database': 'cadastro',
        'user': 'root',
        'password': ''
        }
 
def criar_conexao():
    return mysql.connector.connect(**config)

def fechar_conexao(con):
    con.close()

def cadastra_nota(chave_acesso, numero, serie, idfornecedor, data_aquisicao):
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        
        nota_sel_id = 0
        
        cursor.execute('set @nota_sel_id = 0;')
        params = [chave_acesso, numero, serie, idfornecedor, data_aquisicao, '@nota_sel_id']
        resultado = cursor.callproc('cadastra_nota', params)
        
        nota_sel_id = resultado[5]
        
        conn.commit()
        
        return nota_sel_id
    except Exception as e:
        print('verifique os valores digitados', e)
    finally:
        cursor.close()
        fechar_conexao(conn)

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

def deletar_patrimonio(idpatrimonio):
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        cursor.execute('delete from patrimonios where idpatrimonio = %s', (idpatrimonio,))
        conn.commit()
    except Exception as e:
        print('Erro ao excluir: ', e)        
    finally:
        print(f'Patrimônio {idpatrimonio} deletado!')
        cursor.close()
        fechar_conexao(conn)

class bank_acess():
    def __init__(self):
        super().__init__()
        self.user = self.user
        self.cargo = self.cargo
        self.type = self.type
    def login(self):
        pass

    def register(self):
        self.user = self.user_edit_line.text()
        self.name = self.name_edit_line.text()
        self.passw = self.pass_edit_line.text()
        self.email = self.email_edit_line.text()
        self.cargo = ''
        
        


        pass

    def menu(self):
        pass

    def exit(self):
        pass

    def clear(self):
        pass

    def search(self):
        pass

    def edit(self):
        pass

    def delete(self):
        pass

    def info(self):
        pass

    def home(self):
        pass
