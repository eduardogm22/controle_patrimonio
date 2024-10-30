# Arquivo para conexão e funções que interagem com o banco de dados
import mysql.connector # type: ignore
from PyQt5.QtGui import QStandardItemModel, QStandardItem


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
