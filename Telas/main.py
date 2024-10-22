from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from cadastro_interface import Ui_cadastro
from query_teste_sqlite import sqlite_db
#import cx_Oracle
import mysql.connector
from mysql.connector import Error

#classe que conecta os botões de limpar e adicionar às suas funções
class cadastro(QtWidgets.QMainWindow):
    def __init__(self, *args, **argvs): #mostrar_dados colocar dps q criar
        super(cadastro, self).__init__(*args, **argvs)
        self.ui = Ui_cadastro()
        self.ui.setupUi(self)
        self.ui.btn_salvar.clicked.connect(self.salvar_dados)
        #self.ui.btn_salvar.clicked.connect(self.limpar_campos)
        self.ui.btn_limpar.clicked.connect(self.limpar_campos)
        #self.atualizar = mostrar_dados

    #função que serve para coletar os dados digitados pelo usuário e registrar no banco de dados.
    '''def add(self):
        db = sqlite_db("Patrimonio.db")
        
        #idInput = self.lineEdit_cadastro_id.text()
        nomeInput = self.ui.lineEdit_cadastro_nome.text()
        grupoInput = self.ui.lineEdit_cadastro_grupo.text()
        descricaoInput = self.ui.lineEdit_cadastro_descricao.text()
        nSerieInput = self.ui.lineEdit_cadastro_nSerie.text()
        dAquisicaoInput = self.ui.lineEdit_cadastro_dAquisicao.text()
        vAquisicaoInput = self.ui.lineEdit_cadastro_vAquisicao.text()
        vidaInput = self.ui.lineEdit_cadastro_vida.text()
        localinput = self.ui.lineEdit_cadastro_local.text()
        notaInput = self.ui.lineEdit_cadastro_nota.text()
        
        
        if nomeInput == "" or grupoInput == "":
            QMessageBox.information(self, "Atenção!", "Preencha os campos obrigatorios!")
        else:
            db.cadastra_apaga_edita("INSERT INTO patrimonio(nome, grupo, descricao, nSerie, dAquisicao, vAquisicao, vida, local, nota) VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
                nomeInput, grupoInput, descricaoInput, nSerieInput, dAquisicaoInput, vAquisicaoInput, vidaInput, localinput, notaInput))
            QMessageBox.information(self, "Cadastro bem sucedido!", "Produto cadastrado com sucesso!")'''
            
    #Função para limpar os dados na tela de controle de patrimonio''
    def limpar_campos(self):
        self.ui.lineEdit_cadastro_id.clear()
        self.ui.lineEdit_cadastro_nome.clear()
        self.ui.lineEdit_cadastro_grupo.clear()
        self.ui.lineEdit_cadastro_descricao.clear()
        self.ui.lineEdit_cadastro_nSerie.clear()
        self.ui.lineEdit_cadastro_dAquisicao.clear()
        self.ui.lineEdit_cadastro_vAquisicao.clear()
        self.ui.lineEdit_cadastro_vida.clear()
        self.ui.lineEdit_cadastro_local.clear()
        self.ui.lineEdit_cadastro_nota.clear()

    """#Função para salvar os dados no banco de dados Oracle
    def salvar_dados(self):
        id = self.ui.lineEdit_cadastro_id.text()
        nome = self.ui.lineEdit_cadastro_nome.text()
        grupo = self.ui.lineEdit_cadastro_grupo.text()
        descricao = self.ui.lineEdit_cadastro_descricao.text()
        nserie = self.ui.lineEdit_cadastro_nSerie.text()
        dt_aqs = self.ui.lineEdit_cadastro_dAquisicao.text()
        vl_aqs = self.ui.lineEdit_cadastro_vAquisicao.text()
        vida = self.ui.lineEdit_cadastro_vida.text()
        local = self.ui.lineEdit_cadastro_local.text()
        nf = self.ui.lineEdit_cadastro_nota.text()

        cursor = None
        connection = None

        try:
            username = "cont"
            password = "cont"
            host = "localhost"
            port = 1521
            service_name = "xepdb1"

            dsn = cx_Oracle.makedsn(host, port, service_name=service_name)
            connection = cx_Oracle.connect(username, password, dsn)
            cursor = connection.cursor()

            cursor.execute(
                "INSERT INTO patrimonio(COD, NOME_ITEM, GRUPO, DESCRICAO, NUM_SERIE, DT_AQS, VL_AQS, VD_UTIL, LOCAL, NF)"
                "VALUES(:COD, :NOME_ITEM, :GRUPO, :DESCRICAO, :NUM_SERIE, :DT_AQS, :VL_AQS, :VD_UTIL, :LOCAL, :NF)",
                {
                    "COD": id,
                    "NOME_ITEM": nome,
                    "GRUPO": grupo,
                    "DESCRICAO": descricao,
                    "NUM_SERIE": nserie,
                    "DT_AQS": dt_aqs,
                    "VL_AQS": vl_aqs,
                    "VD_UTIL": vida,
                    "LOCAL": local,
                    "NF": nf
                }
            )

            connection.commit()
            QMessageBox.information(None, "Dados salvos com sucesso!", "Os dados foram salvos com sucesso!")

            self.limpar_campos()

        except cx_Oracle.DatabaseError as e:
            error, = e.args
            print("Erro banco de dados: {} - {}".format(error.code, error.message))

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()"""
    
    #Função para salvar os dados no banco de dados MySQL
    def salvar_dados(self):
        id = self.ui.lineEdit_cadastro_id.text()
        nome = self.ui.lineEdit_cadastro_nome.text()
        grupo = self.ui.lineEdit_cadastro_grupo.text()
        descricao = self.ui.lineEdit_cadastro_descricao.text()
        nserie = self.ui.lineEdit_cadastro_nSerie.text()
        dt_aqs = self.ui.lineEdit_cadastro_dAquisicao.text()
        vl_aqs = self.ui.lineEdit_cadastro_vAquisicao.text()
        vida = self.ui.lineEdit_cadastro_vida.text()
        locl = self.ui.lineEdit_cadastro_local.text()
        nf = self.ui.lineEdit_cadastro_nota.text()

        cursor = None
        connection = None

        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="cont",
                password="cont",
                database="patrimonio"
            )

            if connection.is_connected():
                cursor = connection.cursor()

                cursor.execute(
                    """INSERT INTO cadastro(ID, NOME, GRUPO, DESCRICAO, NUM_SERIE, DT_AQS, VL_AQS, VD_UTIL, LOCL, NF)
                    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                    (id, nome, grupo, descricao, nserie, dt_aqs, vl_aqs, vida, locl, nf)
                )

                connection.commit()
                QMessageBox.information(None, "Dados salvos com sucesso!", "Os dados foram salvos com sucesso!")

                self.limpar_campos()

        except Error as e:
            print("Erro banco de dados: {}".format(e))

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()


            
#utilizada para abrir a página
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = cadastro()
    window.show()
    sys.exit(app.exec_())