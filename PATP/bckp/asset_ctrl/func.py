# funcionalidades de cada tela que for chamada

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QFrame,QWidget, QLabel, QGraphicsDropShadowEffect, QAbstractItemView
from PyQt5.QtWidgets import QWidget,QPushButton,QFrame,QLineEdit, QComboBox, QDateEdit, QFocusFrame, QScrollArea, QVBoxLayout, QSpinBox, QTableView, QSizePolicy, QHeaderView,QDialog, QListView, QListWidget, QGraphicsView, QGraphicsScene, QFileDialog, QMessageBox, QTextBrowser, QCheckBox
from PyQt5 import uic, QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QResource , QTimer, QLocale, QSortFilterProxyModel, pyqtSignal
from PyQt5.QtGui import QIcon, QFocusEvent,QDoubleValidator, QStandardItemModel, QStandardItem, QFont
from connect import conecta_procedure_tela, criar_conexao, fechar_conexao, config_acess, config
import mysql.connector # type: ignore
from PyQt5.QtGui import QDoubleValidator, QKeyEvent
from PyQt5.QtCore import Qt
import matplotlib.pyplot as plt # type: ignore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas # type: ignore
from matplotlib.figure import Figure # type: ignore
import pandas as pd
from datetime import datetime,timedelta
import os, json
import openpyxl #type: ignore
from openpyxl.styles import Font, Alignment #type: ignore
from PyQt5.QtSql import QSqlQueryModel
import traceback

id_user = ''
data_user = ''
data_pass = ''
data_cargo = 15
if os.path.exists('line/dados.json'):
    print("Arquivo JSON existe.")
    v_j = json.load(open("line/dados.json"))
    id_user = v_j["idusuario"]
    data_user = v_j["user"]
    data_pass = v_j["password"]
    data_cargo = v_j["cargo"]
    print('Usuário:', data_user, 'Senha:', data_pass, 'Cargo:', data_cargo ,'func')
else:
    print("Arquivo JSON inexistente func.")

# icones svg
QResource.registerResource("feather/resource.qrc")
home_svg = QIcon("feather/home.svg")
chevrons_left_svg = QIcon("feather/chevrons-left.svg")
menu_svg = QIcon("feather/menu.svg")
user_svg = QIcon("feather/user.svg")
codesandbox_svg = QIcon("feather/codesandbox.svg")
database_svg = QIcon("feather/database.svg")
map_pin_svg = QIcon("feather/map-pin.svg")
dollar_sign_svg = QIcon("feather/dollar-sign.svg")
server_svg = QIcon("feather/server.svg")
search_svg = QIcon("feather/search.svg")
alert_circle_svg = QIcon("feather/alert-circle.svg")
file_text_svg = QIcon("feather/file-text.svg")
users_svg = QIcon("feather/users.svg")
shopping_bag = QIcon("feather/shopping-bag.svg")
activity_svg = QIcon("feather/activity.svg")
save_svg = QIcon("feather/save.svg")
help_circle_svg = QIcon("feather/help-circle.svg")
link_svg = QIcon("feather/link.svg")
user_plus_svg = QIcon("feather/user-plus.svg")
edit_svg = QIcon("feather/edit.svg")
info_svg = QIcon("feather/info.svg")
trash_svg = QIcon("feather/trash.svg")



# Classe do menu usuários, com as funções de cada botão
class user_menu(QWidget):
    def __init__(self):
        super().__init__()
        self.user_main = uic.loadUi("templates/interfaces/user_main.ui", self)
        self.btn_search = self.findChild(QPushButton,"btnSearch")
        self.btn_search.setIcon(search_svg)
        self.search_frame = self.findChild(QFrame, "search_frame")
        self.btn_search.installEventFilter(self)        
        
        self.btn_cad = self.findChild(QPushButton, "btnCad")
        self.btn_cad.setIcon(user_plus_svg)
        self.cad_frame = self.findChild(QFrame, "cadFrame")
        self.btn_cad.installEventFilter(self)

        self.btn_info = self.findChild(QPushButton, "btnDetails")
        self.btn_info.setIcon(info_svg)
        self.info_frame = self.findChild(QFrame, "infoFrame")
        self.btn_info.installEventFilter(self)
        
        self.table_user = self.findChild(QTableView, "l_user")
        self.table_logs = self.findChild(QTableView, "logsReg")
        self.search_line = self.findChild(QLineEdit, "search_input")

        self.frame_user = self.findChild(QFrame, "info_user")

        self.btn_search.clicked.connect(self.search)
        self.btn_cad.clicked.connect(self.register)
        self.btn_info.clicked.connect(self.info)
        
        self.shadow_user1 = QGraphicsDropShadowEffect() 
        self.shadow_user1.setOffset(0, 0)
        self.shadow_user1.setBlurRadius(9)
        self.shadow_user1.setColor(QtGui.QColor(0, 0, 0, 128))

        self.shadow_user2 = QGraphicsDropShadowEffect() 
        self.shadow_user2.setOffset(0, 0)
        self.shadow_user2.setBlurRadius(9)
        self.shadow_user2.setColor(QtGui.QColor(0, 0, 0, 128))

        self.shadow_user3 = QGraphicsDropShadowEffect() 
        self.shadow_user3.setOffset(0, 0)
        self.shadow_user3.setBlurRadius(9)
        self.shadow_user3.setColor(QtGui.QColor(0, 0, 0, 128))

        self.shadow_user4 = QGraphicsDropShadowEffect() 
        self.shadow_user4.setOffset(0, 0)
        self.shadow_user4.setBlurRadius(9)
        self.shadow_user4.setColor(QtGui.QColor(0, 0, 0, 128))

        self.shadow_user5 = QGraphicsDropShadowEffect() 
        self.shadow_user5.setOffset(0, 0)
        self.shadow_user5.setBlurRadius(9)
        self.shadow_user5.setColor(QtGui.QColor(0, 0, 0, 128))

        self.shadow_user6 = QGraphicsDropShadowEffect() 
        self.shadow_user6.setOffset(0, 0)
        self.shadow_user6.setBlurRadius(9)
        self.shadow_user6.setColor(QtGui.QColor(0, 0, 0, 128))

        self.head_frame = self.findChild(QFrame, "header_user_frame")

        con_u = mysql.connector.connect(**config_acess)
        cursor_u = con_u.cursor()
        print(type(cursor_u))
        cursor_u.execute("""select u.usuario, c.nome AS cargo_nome, p.nome AS pessoa_nome, p.dt_create from usuarios u join cargos c on u.idcargo = c.idcargo join pessoas p on u.idpessoa = p.idpessoa where u.idpessoa = p.idpessoa;""")
        self.results_u = cursor_u.fetchall()
         # Criar o modelo para o QTableView
        model_u = QStandardItemModel(len(self.results_u), 4)  # (número de linhas, número de colunas)

        for row_idx, row_data in enumerate(self.results_u):
            for col_idx, data in enumerate(row_data):
                item = QStandardItem(str(data))
                item.setFont(QFont("Roboto", 9))
                item.setTextAlignment(Qt.AlignCenter)
                model_u.setItem(row_idx, col_idx, item)
        header = self.table_user.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        header.setStretchLastSection(True)
        self.table_user.setModel(model_u)
        self.table_user.setGridStyle(Qt.NoPen)
        #self.table_view.setHorizontalHeader(None)
        self.table_user.setAlternatingRowColors(True)
        self.table_user.setStyleSheet("alternate-background-color: #F0F0F0; background-color: #FFFFFF;")
        self.table_user.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_user.setEditTriggers(QAbstractItemView.NoEditTriggers)
            
    def register(self):
        self.c_frame = self.findChild(QFrame, "createFrame")
        self.u_frame = self.findChild(QFrame, "userFrame")
        self.user_create = uic.loadUi("templates/interfaces/user_create.ui")
        self.c_frame.layout().addWidget(self.user_create)
        self.btn_clear = self.findChild(QPushButton, "btnClear")
        self.btn_clear.clicked.connect(self.clear)
        self.btn_confirm = self.findChild(QPushButton, "btnConfirm")
        self.btn_confirm.clicked.connect(self.create_user)
        self.frame_bot = self.findChild(QFrame, "frame_bottom")
        self.frame_body = self.findChild(QFrame, "frame_body")  
        self.cargo_box = self.findChild(QComboBox, "cargoBox")
        self.cargo_box.setStyleSheet("QComboBox#cargoBox{border: 1px solid #000000;} QComboBox#cargoBox::drop-down{border: 1px solid #000000; border-radius:9px;}")
        
        self.user_edit_line = self.findChild(QLineEdit, "userEdit")
        self.name_edit_line = self.findChild(QLineEdit, "nameEdit")
        self.pass_edit_line = self.findChild(QLineEdit, "passEdit")
        self.email_edit_line = self.findChild(QLineEdit, "emailEdit")

        self.frame_btns = self.findChild(QFrame, "frame_btns")
        self.frame_back = self.findChild(QFrame, "frame_back")

        
        self.shadow_details = QGraphicsDropShadowEffect() 
        self.shadow_details.setOffset(0, 0)
        self.shadow_details.setBlurRadius(9)
        self.shadow_details.setColor(QtGui.QColor(0, 0, 0, 128))
    
        self.shadow_f1 = QGraphicsDropShadowEffect() 
        self.shadow_f1.setOffset(0, 0)
        self.shadow_f1.setBlurRadius(9)
        self.shadow_f1.setColor(QtGui.QColor(0, 0, 0, 128))

        self.shadow_f2 = QGraphicsDropShadowEffect() 
        self.shadow_f2.setOffset(0, 0)
        self.shadow_f2.setBlurRadius(9)
        self.shadow_f2.setColor(QtGui.QColor(0, 0, 0, 128))

        self.shadow_f3 = QGraphicsDropShadowEffect() 
        self.shadow_f3.setOffset(0, 0)
        self.shadow_f3.setBlurRadius(9)
        self.shadow_f3.setColor(QtGui.QColor(0, 0, 0, 128))

        self.shadow_f4 = QGraphicsDropShadowEffect() 
        self.shadow_f4.setOffset(0, 0)
        self.shadow_f4.setBlurRadius(9)
        self.shadow_f4.setColor(QtGui.QColor(0, 0, 0, 128))

        self.shadow_f5 = QGraphicsDropShadowEffect() 
        self.shadow_f5.setOffset(0, 0)
        self.shadow_f5.setBlurRadius(9)
        self.shadow_f5.setColor(QtGui.QColor(0, 0, 0, 128))

        self.shadow_f6 = QGraphicsDropShadowEffect() 
        self.shadow_f6.setOffset(0, 0)
        self.shadow_f6.setBlurRadius(9)
        self.shadow_f6.setColor(QtGui.QColor(0, 0, 0, 128))

        self.shadow_f7 = QGraphicsDropShadowEffect() 
        self.shadow_f7.setOffset(0, 0)
        self.shadow_f7.setBlurRadius(9)
        self.shadow_f7.setColor(QtGui.QColor(0, 0, 0, 128))

        self.user_edit_line.setGraphicsEffect(self.shadow_f1)
        self.name_edit_line.setGraphicsEffect(self.shadow_f2)
        self.pass_edit_line.setGraphicsEffect(self.shadow_f3)
        self.email_edit_line.setGraphicsEffect(self.shadow_f4)
        self.cargo_box.setGraphicsEffect(self.shadow_f5)
        self.frame_btns.setGraphicsEffect(self.shadow_f6)
        self.frame_back.setGraphicsEffect(self.shadow_f7)

        self.frame_bot.setGraphicsEffect(self.shadow_details)
        self.cargo_box.setStyleSheet("QComboBox#cargoBox{text-align: center;}")
        self.u_frame.hide()
        self.c_frame.show()
        con_cargo = mysql.connector.connect(**config)
        cursor2 = con_cargo.cursor()
        query = "SELECT nome FROM cargos"
        cursor2.execute(query)
        dados = cursor2.fetchall()
        for dado in dados:
            self.cargo_box.addItem(dado[0])
        self.u_frame.hide()
        self.c_frame.show()
        con_cargo.close()
    
    def create_user(self):
        user = self.user_edit_line.text()
        name = self.name_edit_line.text()
        passw = self.pass_edit_line.text()
        email = self.email_edit_line.text()
        cargo = self.cargo_box.currentText()
        # faltando lógica para verificar se usuário já existe no banco com o mesmo nome.
        print(user,name,passw,email,cargo)
    
    def eventFilter(self, obj, event):

        if obj == self.btn_search:
            if event.type() == QtCore.QEvent.Enter:
                self.search_frame.setStyleSheet("QPushButton#btnSearch{border:2px solid #666666;border-radius:15px;}")
            elif event.type() == QtCore.QEvent.Leave:
                self.search_frame.setStyleSheet("QPushButton#btnSearch{border: 0px solid transparent;}")

        elif obj == self.btn_cad:
            if event.type() == QtCore.QEvent.Enter:
                self.cad_frame.setStyleSheet("QPushButton#btnCad{border:2px solid #666666;border-radius:15px;}")
            elif event.type() == QtCore.QEvent.Leave:
                self.cad_frame.setStyleSheet("QPushButton#btnCad{border: 0px solid transparent;}")

        elif obj == self.btn_info:
            if event.type() == QtCore.QEvent.Enter:
                self.info_frame.setStyleSheet("QPushButton#btnDetails{border:2px solid #666666;border-radius:15px;}")
            elif event.type() == QtCore.QEvent.Leave:
                self.info_frame.setStyleSheet("QPushButton#btnDetails{border: 0px solid transparent;}")

        return super().eventFilter(obj, event)
    

    def delete(self):
        print('Delete')
    
    def edit(self):
        print('Edit')
    
    def info(self):
        print('Info')
    
    def search(self):
        print('Search')
        
    def clear(self):
        self.user_edit_line = self.findChild(QLineEdit, "userEdit")
        self.name_edit_line = self.findChild(QLineEdit, "nameEdit")
        self.pass_edit_line = self.findChild(QLineEdit, "passEdit")
        self.email_edit_line = self.findChild(QLineEdit, "emailEdit")
        self.user_edit_line.clear() 
        self.name_edit_line.clear()
        self.pass_edit_line.clear()
        self.email_edit_line.clear()
        print('Teste')

class user_info(QWidget):
    def __init__(self):
        super().__init__()
        self.user_info = uic.loadUi("templates/interfaces/user_info.ui", self)




class bag_view(QWidget):
    def __init__(self):
        super().__init__()
        self.bag_screen = uic.loadUi("templates/interfaces/bag.ui", self)
        self.produtos = []
        self.produtos_temporarios = []


        self.btn_add_item = self.findChild(QPushButton, "regItem")
        self.btn_add_item.clicked.connect(self.bag_cad)
        self.btn_add_item.installEventFilter(self)


        self.btn_details = self.findChild(QPushButton, "details_btn")
        self.btn_details.installEventFilter(self)
        self.btn_details.hide()



        self.edit_btn = self.findChild(QPushButton, "edit_btn")
        self.edit_btn.clicked.connect(self.bag_edit)

        self.frame_view = self.findChild(QFrame, "frame_view")
        self.frame_search = self.findChild(QFrame, "frame_search")
        self.frame_edit = self.findChild(QFrame, "frame_edit")
        self.frame_details = self.findChild(QFrame, "frame_detail")


        self.shadow_view = QGraphicsDropShadowEffect() 
        self.shadow_view.setOffset(0, 0)
        self.shadow_view.setBlurRadius(9)
        self.shadow_view.setColor(QtGui.QColor(0, 0, 0, 128))

        self.shadow_search = QGraphicsDropShadowEffect() 
        self.shadow_search.setOffset(0, 0)
        self.shadow_search.setBlurRadius(9)
        self.shadow_search.setColor(QtGui.QColor(0, 0, 0, 128))


        self.shadow_edit = QGraphicsDropShadowEffect() 
        self.shadow_edit.setOffset(0, 0)
        self.shadow_edit.setBlurRadius(9)
        self.shadow_edit.setColor(QtGui.QColor(0, 0, 0, 128))


        self.shadow_detail = QGraphicsDropShadowEffect() 
        self.shadow_detail.setOffset(0, 0)
        self.shadow_detail.setBlurRadius(9)
        self.shadow_detail.setColor(QtGui.QColor(0, 0, 0, 128))

        self.frame_view.setGraphicsEffect(self.shadow_view)
        self.frame_search.setGraphicsEffect(self.shadow_search)
        self.frame_edit.setGraphicsEffect(self.shadow_edit)
        self.frame_details.setGraphicsEffect(self.shadow_detail)
        self.search_line = self.findChild(QLineEdit, "line_search")
        self.table_item = self.findChild(QTableView, "table_bag")
        con = mysql.connector.connect(**config)
        cursor = con.cursor()
        cursor.execute("select idpatrimonio,p.nome as patrimonio_nome,p.data_recebimento,c.nome as categoria_nome,s.nome as setor_nome from patrimonios p left join categorias c ON p.idcategoria = c.idcategoria left join setores_responsaveis s ON p.idsetor_responsavel = s.idsetor_responsavel")
        self.results_mdl = cursor.fetchall()
        self.modelo = QStandardItemModel(len(self.results_mdl), 5)
        for row_idx, row_data in enumerate(self.results_mdl):
            for col_idx, data in enumerate(row_data):
                item = QStandardItem(str(data))
                item.setFont(QFont("Roboto", 12))
                item.setTextAlignment(Qt.AlignCenter)
                self.modelo.setItem(row_idx, col_idx, item)
        header_item = self.table_item.horizontalHeader()
        header_item.setSectionResizeMode(QHeaderView.Stretch)
        header_item.setStretchLastSection(True)
        self.table_item.setModel(self.modelo)        
        self.table_item.verticalHeader().setVisible(False)
        self.table_item.horizontalHeader().setVisible(False)
        self.table_item.resizeColumnsToContents()
        self.table_item.setColumnWidth(1, 250)
        self.table_item.hideColumn(0)
        
        header = self.table_item.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        header.setStretchLastSection(True)
        
        self.table_item.setAlternatingRowColors(True)
        self.table_item.setStyleSheet("alternate-background-color: #F0F0F0; background-color: #FFFFFF;")
        
        self.table_item.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_item.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.selected_rows = []
        self.table_item.clicked.connect(self.handle_row_click)
        

        self.l_t = None
        if self.l_t != None:
            self.btn_details.show()
        else:
            self.btn_details.hide()

        self.verif_cargo()
        self.btn_details.clicked.connect(self.exibir_detalhes)
        self.search_line.textChanged.connect(self.filtrar_dados)
        

    def handle_row_click(self, index):
        self.row = index.row()
        modelo = self.table_item.model()
        item_id = modelo.item(self.row, 0).text()
        print(f"Dados da linha {self.row}: {item_id}")
        self.btn_details.setEnabled(True)
        self.btn_details.show()
        
    def exibir_detalhes(self):
        print('Exibir detalhes: ', self.row)
        modelo_atual = self.table_item.model()
        item_id = modelo_atual.item(self.row, 0).text()
        print(f"ID do item selecionado: {item_id}")

        """Exibir detalhes do item selecionado."""
        if hasattr(self, 'selected_rows'):
            # Recuperar o modelo atualmente exibido
            modelo_atual = self.table_item.model()
            item_id = modelo_atual.item(self.row, 0).text()
            # Recuperar o ID da primeira coluna (mesmo que esteja oculta)
            dialog = detail_window(item_id)
            dialog.exec_()
            print('janela chamada')

    def carregar_dados(self, data, modelo):
        for row_idx, row_data in enumerate(data):
            for col_idx, cell_data in enumerate(row_data):
                item = QStandardItem(str(cell_data))
                item.setFont(QFont("Roboto", 12))
                item.setTextAlignment(Qt.AlignCenter)
                modelo.setItem(row_idx, col_idx, item)
        self.table_item.horizontalHeader().setVisible(False)

    def filtrar_dados(self, texto):
        texto = texto.lower()
        modelo_filtrado = QStandardItemModel(0, 5)
        self.table_item.horizontalHeader().setVisible(False)

        for row in self.results_mdl:
            if any(texto in str(cell).lower() for cell in row):
                items = [QStandardItem(str(cell)) for cell in row]
                for item in items:
                    item.setFont(QFont("Roboto", 12))
                    item.setTextAlignment(Qt.AlignCenter)
                modelo_filtrado.appendRow(items)

        self.table_item.setModel(modelo_filtrado)

    def verif_cargo(self):
        if data_cargo == 4 or data_cargo == 3:
            self.btn_add_item.hide()
            self.edit_btn.hide()        
        else:
            pass
        
    def bag_edit(self):
        modelo = self.table_item.model()
        item_id = modelo.item(self.row, 0).text()
        self.edit_itens = bag_edit(item_id)
        self.edit_frame = self.findChild(QFrame, "frame_edit_2")
        self.body_frame = self.findChild(QFrame, "frame_2")
        self.edit_frame.layout().addWidget(self.edit_itens)
        self.btn_teste = self.findChild(QPushButton, "test")
        self.body_frame.hide()
        self.edit_frame.show()

    def eventFilter(self, obj, event):
        pass
        return super().eventFilter(obj, event)
    def lista_itens(self):
        pass
    def bag_cad(self):
        self.cad_itens = bag_item_cad()
        self.cad_frame = self.findChild(QFrame, "frame_edit_2")
        self.body_frame = self.findChild(QFrame, "frame_2")
        self.cad_frame.layout().addWidget(self.cad_itens)
        self.btn_teste = self.findChild(QPushButton, "test")
        self.body_frame.hide()
        self.cad_frame.show()       


class bag_edit(QWidget):
    def __init__(self, id_item):
        super().__init__()
        self.edit = uic.loadUi("templates/interfaces/item_edit.ui", self)
        self.id_item = id_item
        self.n_item = self.findChild(QLabel, "label")
        self.n_item.setText(f"Item: {self.id_item}")
        self.n_f = self.findChild(QLineEdit, "chave_acesso")
        self.n_s = self.findChild(QLineEdit, "n_serie")
        self.n_n = self.findChild(QLineEdit, "n_nota")
        self.name_p = self.findChild(QLineEdit, "name_prod")
        self.v_u = self.findChild(QLineEdit, "value_prod")  
        self.c_sit = self.findChild(QComboBox, "c_sit")
        self.c_set = self.findChild(QComboBox, "c_setor")
        self.c_item = self.findChild(QComboBox, "cat_item")
        self.local_i = self.findChild(QComboBox, 'local_item')
        self.del_btn = self.findChild(QPushButton, "del_item")
        self.edit_btn = self.findChild(QPushButton, "edit_item")
        self.return_btn = self.findChild(QPushButton, "return_btn")
        self.dt_buy = self.findChild(QDateEdit, "date_buy")
        self.dt_rec = self.findChild(QDateEdit, "date_rec")
        self.del_btn.clicked.connect(self.deletar_item)
        
    def deletar_item(self):
        print(self.id_item)



class bag_item_cad(QWidget):
    def __init__(self):
        super().__init__()
        
        self.cad_item = uic.loadUi("templates/interfaces/bag_item_cad.ui", self)
        self.name_item = self.findChild(QLineEdit, "name_prod");        
        self.quantidade = self.findChild(QSpinBox, "qnt")
        self.categ_item = self.findChild(QComboBox, "cat_item")
        self.dt_rec = self.findChild(QDateEdit, "date_rec")
        self.setor_item = self.findChild(QComboBox, "c_setor")
        self.sit_item = self.findChild(QComboBox, "c_sit")
        self.rec_por = self.findChild(QLineEdit, "rec_p")
        self.chave_acesso = self.findChild(QLineEdit, "chave_acesso")
        self.n_nota = self.findChild(QLineEdit, "n_nota")
        self.n_serie = self.findChild(QLineEdit, "n_serie")
        self.forn_name = self.findChild(QComboBox, "forn_name")
        self.date_buy = self.findChild(QDateEdit, "date_buy")
        self.date_rec = self.findChild(QDateEdit, "date_rec")
        today = datetime.now()
        self.date_buy.setDate(today)
        self.date_rec.setDate(today)

        self.btn_cancel = self.findChild(QPushButton, "cancelBtn")
        self.btn_cancel.clicked.connect(self.cancel_event)
        #colocando as categorias na combo box
        con = criar_conexao()
        cursor = con.cursor()
        cursor.execute('select nome from categorias order by nome')
        resultado = cursor.fetchall()
        for dados in resultado:
            self.categ_item.addItem(dados[0])
            
        cursor.execute('select nome from fornecedores order by nome')
        resultado_forn = cursor.fetchall()
        for dados in resultado_forn:
            self.forn_name.addItem(dados[0])
            
        cursor.execute('select nome from setores_responsaveis order by nome')
        resultado_set_resp = cursor.fetchall()
        for dados in resultado_set_resp:
            self.setor_item.addItem(dados[0])
            
        cursor.execute('select nome from situacoes order by nome')
        resultado_situacoes = cursor.fetchall()
        for dados in resultado_situacoes:
            self.sit_item.addItem(dados[0])
            

        cursor.close()
        fechar_conexao(con)

        # filtro para o campo de valor, aplicada regras para não aceitar virgula e nem outros digitos.
        self.number_input = self.findChild(QLineEdit, "value_prod")
        validator = QDoubleValidator(0.0, 10000.0, 2)
        validator.setNotation(QDoubleValidator.StandardNotation)
        validator.setLocale(self.number_input.locale())
        locale = QLocale(QLocale.C)
        validator.setLocale(locale)
        self.number_input.setValidator(validator)
        self.btn_ok = self.findChild(QPushButton, "ok_btn")
        self.number_input.keyPressEvent = self.keyPressEvent
        self.btn_confirm = self.findChild(QPushButton, "cadItens")
        self.btn_confirm.clicked.connect(self.confirm)

        self.del_btn = self.findChild(QPushButton, "del")
        self.del_btn.clicked.connect(self.deletar_item)

        self.listagem = {}
        self.id_counter = 0
        self.lista_produtos = self.findChild(QTableView, "list_itens_add")

        self.btn_ok.clicked.connect(self.temp_list)

        self.selected_row = None

        self.lista_produtos.clicked.connect(self.handle_row_click)
        self.selected_rows = []
        self.lista_produtos.setGridStyle(Qt.NoPen)
        self.lista_produtos.setAlternatingRowColors(True)
        self.lista_produtos.setStyleSheet("alternate-background-color: #F0F0F0; background-color: #FFFFFF;")
        self.lista_produtos.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.lista_produtos.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.value_result = self.findChild(QLabel, "value_r")

        self.number_input.textChanged.connect(self.update_label)
        self.quantidade.valueChanged.connect(self.update_label)

        self.atualizar_tabela()


    def cancel_event(self):
        self.rec_por.clear()
        self.quantidade.clear()
        self.name_item.clear()
        self.number_input.clear()
        self.categ_item.setCurrentIndex(0)
        self.chave_acesso.clear()
        self.n_nota.clear()
        self.n_serie.clear()
        self.forn_name.setCurrentIndex(0)
        self.date_buy.setDate(datetime.now())
        self.date_rec.setDate(datetime.now())
        self.setor_item.setCurrentIndex(0)
        self.sit_item.setCurrentIndex(0)

    def update_label(self):
        try:
            valor = float(self.number_input.text() if self.number_input.text() else 0)
            q = float(self.quantidade.value())
            v = float(valor)
            resultado = q * v
            self.value_result.setText(f"Valor Total: {resultado:.2f}")
        except ValueError:
            self.value_result.setText("Por favor, insira um número válido no campo de valor.")
        pass
    

    def temp_list(self):
        nome = self.name_item.text().strip()
        valor = self.number_input.text()
        categoria = self.categ_item.currentText()
        quantidade = self.quantidade.value()

        data_aquisicao = self.date_buy.date().toString("yyyy-MM-dd")
        chave_acesso = self.chave_acesso.text()
        numero = self.n_nota.text()
        serie = self.n_serie.text()

        print(chave_acesso)

        con = criar_conexao()
        cursor = con.cursor()
        cursor.execute('SELECT idfornecedor FROM fornecedores WHERE nome = %s', (self.forn_name.currentText(),))
        fornecedor_id = cursor.fetchone()[0]
        
        cursor.execute('SELECT nome FROM setores_responsaveis WHERE nome = %s', (self.setor_item.currentText(),))
        setor_nome = cursor.fetchone()[0]
        
        cursor.execute('SELECT nome FROM situacoes WHERE nome = %s', (self.sit_item.currentText(),))
        situacao = cursor.fetchone()[0]
        
        cursor.close()
        fechar_conexao(con)

        if not nome or not valor or quantidade == 0 or not chave_acesso or not numero or not serie or not data_aquisicao:
            print('Faltando valores. Verifique!')
        else:
            self.id_counter += 1
            self.listagem[self.id_counter] = [nome, valor, categoria, quantidade, setor_nome, situacao]
            self.atualizar_tabela()
            self.clear_c()

            # Armazena os dados da nota fiscal
            self.chave_acesso_temp = chave_acesso
            self.numero_nota_temp = numero
            self.serie_nota_temp = serie
            self.data_aquisicao_temp = data_aquisicao
            self.forn_sel_id = fornecedor_id
            # Não insere os itens agora, só guarda na lista local
            print(f'Itens para cadastro: {self.listagem}')

        
    def clear_c(self):
        self.name_item.clear()
        self.number_input.clear()
        self.quantidade.clear()
        self.quantidade.setValue(0)

    def clear_u(self):
        self.name_item.clear()
        self.number_input.clear()
        self.quantidade.clear()
        self.quantidade.setValue(0)
        self.forn_name.setCurrentIndex(0)
        self.setor_item.setCurrentIndex(0)
        self.sit_item.setCurrentIndex(0)
        self.lista_produtos.clearSelection()
        self.listagem.clear()
        self.chave_acesso.clear()
        self.n_nota.clear()
        self.n_serie.clear()
        self.date_buy.setDate(datetime.now())
        self.date_rec.setDate(datetime.now())
        self.atualizar_tabela()

    def atualizar_tabela(self):
        mdl = QStandardItemModel()
        hdr = ["Nome", "Valor", "Categoria", "Quantidade", "Setor", "Situação"]
        mdl.setHorizontalHeaderLabels(hdr)
        for item_id, item_data in self.listagem.items():
            row_items = []
            for value in item_data:
                item = QStandardItem(str(value))
                row_items.append(item)
            mdl.appendRow(row_items)
        self.lista_produtos.setModel(mdl)
        self.lista_produtos.verticalHeader().setVisible(False)
        self.lista_produtos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        self.lista_produtos.horizontalHeader().setStretchLastSection(True)
        print(self.listagem)
        
                
    # função responsável pela interação de seleção de linha
    # print com o for apenas para teste
    def handle_row_click(self, index):
        row = index.row()
        self.selected_row = row
        print(f"Dados da linha {row}:")
        for column in range(self.lista_produtos.model().columnCount()):
            data = self.lista_produtos.model().index(row, column).data()
            print(f"{self.lista_produtos.model()}: {data}")
        self.selected_rows.clear()
        self.selected_rows.append(self.lista_produtos.model().index(row, column).data())
        
    def deletar_item(self):
        if self.selected_row is None:
            print("Nenhuma linha selecionada para deletar.")
            return
        item_id = list(self.listagem.keys())[self.selected_row]
        del self.listagem[item_id]
        self.atualizar_tabela()
        self.selected_row = None
        if self.listagem:
            self.id_counter = max(self.listagem.keys())
        else:
            self.id_counter = 0

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Comma:
            return
        QLineEdit.keyPressEvent(self.number_input, event)
        


    def confirm(self):
        print("Confirmando os itens:", self.listagem)
        print (self.chave_acesso_temp)
        con = criar_conexao()
        cursor = con.cursor()
        cursor.execute('SELECT chave_acesso FROM info_notas WHERE chave_acesso = %s', (self.chave_acesso_temp,))
        chave_acesso_existente = cursor.fetchone()
        cursor.close()
        fechar_conexao(con)

        if chave_acesso_existente:
            print("Nota fiscal ja cadastrada")
            QMessageBox.warning(self, "Erro", "Nota fiscal ja cadastrada")
            self.clear_u()
            return        


        con = criar_conexao()
        cursor = con.cursor()

        try:
            # Insere a nota fiscal na tabela info_notas
            print("Inserindo nota fiscal...")
            cursor.execute('''
                INSERT INTO info_notas (chave_acesso, numero, serie, idfornecedor, data_aquisicao)
                VALUES (%s, %s, %s, %s, %s)
            ''', (self.chave_acesso_temp, self.numero_nota_temp, self.serie_nota_temp, self.forn_sel_id, self.data_aquisicao_temp))
            
            con.commit()
            print("Nota fiscal inserida com sucesso.")

            # Recupera o idnota da nota fiscal recém inserida
            print("Recuperando ID da nota fiscal...")
            cursor.execute('SELECT idnota FROM info_notas WHERE chave_acesso = %s', (self.chave_acesso_temp,))
            id_nota = cursor.fetchone()[0]
            print(f"ID da nota fiscal: {id_nota}")

            # toda a seção for foi usado prints para poder verificar se estava indo certo, e onde poderia ocorrer algum erro ou bug.

            # Processa cada item na listagem
            for item_id, item_data in self.listagem.items():
                try:
                    nome, valor_unitario, categoria, quantidade,setor_nome, situacao = item_data
                    print(f"Processando item: ID={item_id}, Nome={nome}, Valor={valor_unitario}, Categoria={categoria}, Quantidade={quantidade} Setor={setor_nome}, Situação={situacao}")

                    # ID categoria
                    print(f"Buscando ID da categoria para '{categoria}'...")
                    cursor.execute('SELECT idcategoria FROM categorias WHERE nome = %s', (categoria,))
                    resultado_cat = cursor.fetchone()
                    if resultado_cat is None:
                        raise ValueError(f"Categoria '{categoria}' não encontrada no banco de dados.")
                    id_categoria = resultado_cat[0]

                    #id do setor responsável
                    setor_nome = self.setor_item.currentText()
                    print(f"Buscando ID do setor responsável para '{setor_nome}'...")
                    cursor.execute('SELECT idsetor_responsavel FROM setores_responsaveis WHERE nome = %s', (setor_nome,))
                    resultado_setor = cursor.fetchone()
                    if resultado_setor is None:
                        raise ValueError(f"Setor '{setor_nome}' não encontrado no banco de dados.")
                    id_setor_responsavel = resultado_setor[0]

                    #obter o ID da situação
                    situacao_nome = self.sit_item.currentText()
                    print(f"Buscando ID da situação para '{situacao_nome}'...")
                    cursor.execute('SELECT idsituacao FROM situacoes WHERE nome = %s', (situacao_nome,))
                    resultado_situacao = cursor.fetchone()
                    if resultado_situacao is None:
                        raise ValueError(f"Situação '{situacao_nome}' não encontrada no banco de dados.")
                    id_situacao = resultado_situacao[0]

                    serie_patrimonio = ''
                    # Insere cada unidade do produto individualmente pela quantidade resgatada do item
                    for _ in range(quantidade):
                        cursor.execute('''
                            INSERT INTO patrimonios (nome, valor_unitario, data_recebimento, idnota, idcategoria, idsetor_responsavel, idsituacao, num_serie)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                        ''', (nome, valor_unitario, self.data_aquisicao_temp, id_nota, id_categoria, id_setor_responsavel, id_situacao, serie_patrimonio))
                    print(f"Item {item_id} inserido com sucesso.")
                # prints do erro
                except Exception as item_error:
                    print(f"Erro ao processar item {item_id}: {item_error}")
                    traceback.print_exc()

            con.commit()
            print(f'{len(self.listagem)} itens e a nota foram cadastrados com sucesso!')

        except Exception as e:
            print('Erro ao cadastrar a nota ou os itens:', e)
            traceback.print_exc()
            con.rollback()

        finally:
            cursor.close()
            fechar_conexao(con)


        
class items_view(QWidget):
    def __init__(self, interface):
        super().__init__()
        self.interface = interface
        self.item_view = uic.loadUi("templates/interfaces/item_view.ui", self)
        self.btn_categ = self.findChild(QPushButton, "cat_item_btn")
        self.btn_categ.clicked.connect(self.categ_view)
        self.tb_item = self.findChild(QTableView, "tb_item")
        self.ct_view = self.findChild(QTableView, "ct_view")
        self.list_itens = self.findChild(QListView, "list_itens")
        self.load_items()

    def load_items(self):
        # Conectar ao banco de dados usando o dicionário config
        conn = mysql.connector.connect(**config)  # Dicionário config já definido
        cursor = conn.cursor()

        # Executar a consulta para buscar os dados
        query = """
        SELECT 
            ptr.nome AS Produto,
            cat.nome AS Categoria,
            sit.nome AS Situação,
            srp.nome AS Setor_Responsável
        FROM 
            patrimonios AS ptr
        INNER JOIN 
            categorias AS cat ON ptr.idcategoria = cat.idcategoria
        INNER JOIN 
            situacoes AS sit ON ptr.idsituacao = sit.idsituacao
        INNER JOIN 
            setores_responsaveis AS srp ON ptr.idsetor_responsavel = srp.idsetor_responsavel;
        """
        cursor.execute(query)
        results = cursor.fetchall()

        # Configurar o modelo
        model = QStandardItemModel(len(results), 4)  # (linhas, colunas)
        model.setHorizontalHeaderLabels(['Produto', 'Categoria', 'Situação', 'Setor Responsável'])

        # Preencher o modelo com os dados do banco
        for row_idx, row_data in enumerate(results):
            for col_idx, data in enumerate(row_data):
                item = QStandardItem(str(data))
                item.setFont(QFont("Roboto", 9))
                item.setTextAlignment(Qt.AlignCenter)
                model.setItem(row_idx, col_idx, item)

        # Definir o modelo no QTableView
        self.tb_item.setModel(model)
        self.tb_item.resizeColumnsToContents()
        self.tb_item.setAlternatingRowColors(True)
        self.tb_item.horizontalHeader().setStretchLastSection(True)
        self.tb_item.setStyleSheet("alternate-background-color: #F0F0F0; background-color: #FFFFFF;")
        self.tb_item.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tb_item.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tb_item.setGridStyle(Qt.NoPen)
        # Fechar o cursor e a conexão
        cursor.close()
        conn.close()


    def categ_view(self):
        self.categview = categ_view()
        self.categview.configRequested.connect(self.interface.config_screen)
        self.frame_v1 = self.findChild(QFrame, "body_item")
        self.frame_v2 = self.findChild(QFrame, "frame_view2")
        self.frame_v2.layout().addWidget(self.categview)
        self.frame_v2.show()
        self.frame_v1.hide()
        


class categ_view(QWidget):   
    configRequested = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.item_category = uic.loadUi("templates/interfaces/categ_view.ui", self)
        self.btn_config = self.findChild(QPushButton, "category")
        self.btn_config.clicked.connect(self.on_config_click)
    def on_config_click(self):
        self.configRequested.emit()




class rel_view(QWidget):
    def __init__(self):
        super().__init__()
        self.rel_view = uic.loadUi("templates/interfaces/rel_view.ui", self)
        self.date_i = self.findChild(QDateEdit, "date_i")
        self.date_f = self.findChild(QDateEdit, "date_f")
        self.set_default_dates()

    def set_default_dates(self):
        today = datetime.now()
        three_years_ago = today - timedelta(days=365 * 1)
        self.date_i.setDate(three_years_ago)
        self.date_f.setDate(today)


class patr_view(QWidget):
    def __init__(self):
        super().__init__()
        self.patr_view = uic.loadUi("templates/interfaces/patr_view.ui", self)
        self.list_ptr = self.findChild(QTableView, "list_patr")
        self.grap_view = self.findChild(QGraphicsView, "grap_view")
        self.date_i = self.findChild(QDateEdit, "dt_inicial")
        self.date_f = self.findChild(QDateEdit, "dt_final")
        self.btn_filter = self.findChild(QPushButton, "filter_dt")
        self.btn_rlt = self.findChild(QPushButton, "rlt_btn")
        self.set_default_dates()

    def set_default_dates(self):
        today = datetime.now()
        three_years_ago = today - timedelta(days=365 * 3)
        self.date_i.setDate(three_years_ago)
        self.date_f.setDate(today)



    def rlt_patrimonio(self):
        d_i = self.date_i.date().toString("yyyy-MM-dd")
        d_f = self.date_f.date().toString("yyyy-MM-dd")

        con = criar_conexao()
        cursor = con.cursor()
        cursor.execute("""
            SELECT nome, valor_unitario, num_patrimonio, data_recebimento 
            FROM patrimonios
            WHERE data_recebimento BETWEEN %s AND %s
        """, (d_i, d_f))
        data = cursor.fetchall()

        workbook = openpyxl.Workbook()
        worksheet = workbook.active
        worksheet.title = "Relatório de Patrimônio"

        bold_font = Font(bold=True)
        centered_alignment = Alignment(horizontal='center', vertical='center')

        worksheet['A1'] = 'Nome'
        worksheet['B1'] = 'Valor Unitário'
        worksheet['C1'] = 'Número de Patrimônio'
        worksheet['D1'] = 'Data de Recebimento'
        for col in range(1, 5):
            worksheet.cell(row=1, column=col).font = bold_font
            worksheet.cell(row=1, column=col).alignment = centered_alignment

        row = 2
        for nome, valor_unitario, num_patrimonio, data_recebimento in data:
            worksheet.cell(row=row, column=1, value=nome)
            worksheet.cell(row=row, column=2, value=valor_unitario)
            worksheet.cell(row=row, column=3, value=num_patrimonio)
            worksheet.cell(row=row, column=4, value=data_recebimento)
            row += 1

        # Salvar o arquivo
        file_path, _ = QFileDialog.getSaveFileName(self, "Salvar Relatório", os.path.expanduser("~"), "Arquivos Excel (*.xlsx)")
        if file_path:
            workbook.save(file_path)
            QMessageBox.information(self, "Relatório Gerado", f"O relatório foi salvo em: {file_path}")

class logs_view(QWidget):
    def __init__(self):
        super().__init__()
        self.logs_view = uic.loadUi("templates/interfaces/logs_view.ui", self)

class config_view(QWidget):
    def __init__(self):
        super().__init__()
        self.config_view = uic.loadUi("templates/interfaces/config_screen.ui", self)
    




class local_info(QWidget):
    def __init__(self):
        super().__init__()
        self.local_info = uic.loadUi("templates/interfaces/local_info.ui", self)
        
class detail_window(QDialog):
    def __init__(self, item_id):
        super().__init__()
        print('item_id teste instancia', item_id)
        self.item_id = item_id

        self.setWindowFlags(Qt.Popup| Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_DeleteOnClose)  # Garante que o diálogo será descartado ao fechar
        self.setFixedSize(400, 300)
        self.setStyleSheet("background-color: #f0f0f0; border: 1px solid #ccc; border-radius: 10px;")

        layout = QVBoxLayout()

        try:
            # Conexão com banco de dados
            con = mysql.connector.connect(**config)
            cursor = con.cursor()
            cursor.execute("SELECT * FROM patrimonios WHERE idpatrimonio = %s", (self.item_id,))
            data = cursor.fetchall()
        except mysql.connector.Error as e:
            print("Erro ao conectar ao banco de dados:", e)
            data = []

        if not data:
            print("Nenhum dado foi encontrado na tabela.")
            detail_text = "Nenhum dado foi encontrado na tabela."
        else:
            detail_text = ""
            for row in data:
                detail_text += f"ID: {row[0]}\n"
                detail_text += f"Nome: {row[1]}\n"
                detail_text += f"Valor Unitário: {row[2]}\n"
                detail_text += f"Data de Recebimento: {row[3]}\n"
                detail_text += f"Patrimônio: {row[4]}\n"
        label_mensagem = QLabel(detail_text)
        label_mensagem.setWordWrap(True)
        label_mensagem.setAlignment(Qt.AlignTop)
        layout.addWidget(label_mensagem)

        self.setLayout(layout)

    def mousePressEvent(self, event):
        """Fecha o diálogo se clicar fora dele."""
        if not self.rect().contains(event.pos()):
            self.close()




class config_cargo(QWidget):
    def __init__(self):
        super().__init__()
        self.config_cargo = uic.loadUi("templates/interfaces/cargo_config.ui", self)
        self.box_cargo = self.findChild(QComboBox, "box_cargo")
        self.new_cargo = self.findChild(QLineEdit, "new_cargo")
        self.btn_confirm = self.findChild(QPushButton, "btn_confirm_edit")
        self.btn_cancel = self.findChild(QPushButton, "btn_cancel")
        self.edit_carg = self.findChild(QPushButton, "edit_cargo")
        self.cancel_edit = self.findChild(QPushButton, "btn_edit_cancel")
        self.perm_acess = self.findChild(QCheckBox, "acesso_geral")
        self.perm_reg = self.findChild(QCheckBox, "pode_registrar")
        self.ctrl_adm = self.findChild(QCheckBox, "controle_adm")
        self.ctrl_user = self.findChild(QCheckBox, "controle_usuario")
        self.perm_mod = self.findChild(QCheckBox, "pode_modificar")
        self.perm_read = self.findChild(QCheckBox, "pode_visualizar")
        self.btn_confirm_n = self.findChild(QPushButton, "btn_confirm")
        self.btn_confirm_n.hide()
        self.new_cargo.hide()
        self.btn_confirm.hide()
        self.btn_cancel.hide()
        self.cancel_edit.hide()
        self.btn_add = self.findChild(QPushButton, "add_cargo")
        self.box_cargo.setPlaceholderText("Selecione um cargo")
        # Conexão com o banco para adicionar valores a combobox
        self.con = criar_conexao()
        self.cursor = self.con.cursor()
        self.cursor.execute("SELECT nome FROM cargos")
        data = self.cursor.fetchall()
        for cargo in data:
            self.box_cargo.addItem(cargo[0])
        # Inicialmente, checkboxes desabilitadas
        self.set_checkboxes_enabled(False)

        # Conecta sinais
        self.box_cargo.currentIndexChanged.connect(self.update_checkboxes)
        self.edit_carg.clicked.connect(self.enable_editing)
        self.btn_confirm.clicked.connect(self.save_changes)
        self.cancel_edit.clicked.connect(self.cancel_changes)

        # Armazenar os valores originais para restaurar em caso de cancelamento
        self.original_values = {}
        self.btn_add.clicked.connect(self.test)
        self.btn_add.clicked.connect(self.start_new_cargo)
        self.btn_confirm_n.clicked.connect(self.save_new_cargo)
        self.btn_cancel.clicked.connect(self.cancel_new_cargo)

    def start_new_cargo(self):
        # sub-sessão para criação de um novo cargo
        self.new_cargo.show()
        self.btn_confirm_n.show()
        self.btn_cancel.show()
        self.edit_carg.hide()
        self.box_cargo.setEnabled(False)
        self.clear_checkboxes()
        self.set_checkboxes_enabled(True)

    def cancel_new_cargo(self):
        """Cancelar o processo de criação de um novo cargo e restaurar o estado inicial."""
        self.new_cargo.hide()
        self.btn_confirm_n.hide()
        self.btn_cancel.hide()
        self.edit_carg.show()
        self.box_cargo.setEnabled(True)
        self.clear_checkboxes()
        self.set_checkboxes_enabled(False)
        self.box_cargo.setCurrentIndex(0)

    def save_new_cargo(self):
        """Salvar o novo cargo no banco de dados."""
        cargo_name = self.new_cargo.text().strip()
        if not cargo_name:
            print("Nome do cargo não pode ser vazio.")
            return

        # Verifica se o cargo já existe
        self.cursor.execute("SELECT COUNT(*) FROM cargos WHERE nome = %s", (cargo_name,))
        if self.cursor.fetchone()[0] > 0:
            print("Cargo já existe!")
            return

        # Obtem os valores das permissões do banco em uma tupla
        data = (
            int(self.perm_acess.isChecked()),
            int(self.perm_reg.isChecked()),
            int(self.ctrl_adm.isChecked()),
            int(self.ctrl_user.isChecked()),
            int(self.perm_mod.isChecked()),
            int(self.perm_read.isChecked()),
            cargo_name,
        )

        # Inserir o novo cargo no banco
        self.cursor.execute("""
            INSERT INTO cargos 
            (acesso_geral, pode_registrar, controle_adm, controle_usuario, pode_modificar, pode_visualizar, nome) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, data)
        self.con.commit()

        # atualiza a combobox
        self.box_cargo.addItem(cargo_name)

        # Restaura a interface ao estado inicial
        self.cancel_new_cargo()    


    def test(self):
        cargo = self.box_cargo.currentText()
        self.cursor.execute("""SELECT acesso_geral, pode_registrar, controle_adm, controle_usuario, pode_modificar, pode_visualizar FROM cargos WHERE nome = %s""", (cargo,))
        data = self.cursor.fetchone()
        print(data)

    def set_checkboxes_enabled(self, enabled):
        """Habilitar ou desabilitar as checkboxes."""
        self.perm_acess.setEnabled(enabled)
        self.perm_reg.setEnabled(enabled)
        self.ctrl_adm.setEnabled(enabled)
        self.ctrl_user.setEnabled(enabled)
        self.perm_mod.setEnabled(enabled)
        self.perm_read.setEnabled(enabled)

    def update_checkboxes(self):
        self.clear_checkboxes()  # Garante que as checkbox estejam limpas
        cargo = self.box_cargo.currentText()

        if not cargo or cargo == "Selecione um cargo":
            self.set_checkboxes_enabled(False)
            return
        # verificação dos dados da combobox no banco para realizar as atribuições dos checkbox
        try:
            self.cursor.execute("""
                SELECT acesso_geral, pode_registrar, controle_adm, controle_usuario, 
                    pode_modificar, pode_visualizar
                FROM cargos 
                WHERE nome = %s
            """, (cargo,))
            data = self.cursor.fetchone()

            if data:
                # debugar os dados brutos recebidos, utilizando print
                print(f"Dados crus do banco para cargo {cargo}: {data}")

                # Converte os valores de CHAR(1) para inteiros
                safe_data = [int(value) if value is not None else 0 for value in data]

                # Atualizar as checkboxes com os valores convertidos
                self.perm_acess.setChecked(bool(safe_data[0]))
                self.perm_reg.setChecked(bool(safe_data[1]))
                self.ctrl_adm.setChecked(bool(safe_data[2]))
                self.ctrl_user.setChecked(bool(safe_data[3]))
                self.perm_mod.setChecked(bool(safe_data[4]))
                self.perm_read.setChecked(bool(safe_data[5]))

                # Debug o estado das checkboxes com print
                print(f"Estados das checkboxes para {cargo}: "
                    f"perm_acess={self.perm_acess.isChecked()}, "
                    f"perm_reg={self.perm_reg.isChecked()}, "
                    f"ctrl_adm={self.ctrl_adm.isChecked()}, "
                    f"ctrl_user={self.ctrl_user.isChecked()}, "
                    f"perm_mod={self.perm_mod.isChecked()}, "
                    f"perm_read={self.perm_read.isChecked()}")
            else:
                print(f"Nenhum dado encontrado para o cargo {cargo}")
                self.set_checkboxes_enabled(False)
        except Exception as e:
            print(f"Erro ao buscar dados do cargo: {e}")
            self.clear_checkboxes()
            self.set_checkboxes_enabled(False)



    def clear_checkboxes(self):
        self.perm_acess.setChecked(False)
        self.perm_reg.setChecked(False)
        self.ctrl_adm.setChecked(False)
        self.ctrl_user.setChecked(False)
        self.perm_mod.setChecked(False)
        self.perm_read.setChecked(False)


    def enable_editing(self):
        # Armazenar os valores originais antes de permitir a edição
        self.original_values = {
            "acesso_geral": self.perm_acess.isChecked(),
            "pode_registrar": self.perm_reg.isChecked(),
            "controle_adm": self.ctrl_adm.isChecked(),
            "controle_usuario": self.ctrl_user.isChecked(),
            "pode_modificar": self.perm_mod.isChecked(),
            "pode_visualizar": self.perm_read.isChecked(),
        }

        self.set_checkboxes_enabled(True)
        self.btn_confirm.show()
        self.cancel_edit.show()
        self.edit_carg.hide()


    def save_changes(self):
        """Salvar as alterações no banco de dados."""
        cargo = self.box_cargo.currentText()
        data = (
            int(self.perm_acess.isChecked()),
            int(self.perm_reg.isChecked()),
            int(self.ctrl_adm.isChecked()),
            int(self.ctrl_user.isChecked()),
            int(self.perm_mod.isChecked()),
            int(self.perm_read.isChecked()),
            cargo,
        )
        self.cursor.execute("""
            UPDATE cargos 
            SET acesso_geral = %s, pode_registrar = %s, controle_adm = %s, controle_usuario = %s, pode_modificar = %s, pode_visualizar = %s
            WHERE nome = %s
        """, data)
        self.con.commit()
        self.set_checkboxes_enabled(False)
        self.btn_confirm.hide()
        self.cancel_edit.hide()
        self.edit_carg.show()

    def cancel_changes(self):
        """Restaurar os valores originais em caso de cancelamento."""
        if not self.original_values:
            print("Nenhum valor original armazenado para restaurar.")
            return

        # restaura os valores originais
        self.perm_acess.setChecked(bool(self.original_values.get("acesso_geral", False)))
        self.perm_reg.setChecked(bool(self.original_values.get("pode_registrar", False)))
        self.ctrl_adm.setChecked(bool(self.original_values.get("controle_adm", False)))
        self.ctrl_user.setChecked(bool(self.original_values.get("controle_usuario", False)))
        self.perm_mod.setChecked(bool(self.original_values.get("pode_modificar", False)))
        self.perm_read.setChecked(bool(self.original_values.get("pode_visualizar", False)))

        # retorna para o layout normal da sessão
        self.set_checkboxes_enabled(False)
        self.btn_confirm.hide()
        self.cancel_edit.hide()
        self.edit_carg.show()

class config_cat(QWidget):
    def __init__(self):
        super().__init__()
        self.config_cat = uic.loadUi("templates/interfaces/categ_config.ui", self)
        self.box_cat = self.findChild(QComboBox, "box_cat")
        con = criar_conexao()
        cursor = con.cursor()
        cursor.execute("SELECT nome FROM categorias")
        data = cursor.fetchall()
        con.close()
        for cat in data:
            self.box_cat.addItem(cat[0])
                 

class config_forn(QWidget):
    def __init__(self):
        super().__init__()
        self.config_forn = uic.loadUi("templates/interfaces/forn_config.ui",self)
        self.box_forn = self.findChild(QComboBox, "box_forn")
        con = criar_conexao()
        cursor = con.cursor()
        cursor.execute("SELECT nome FROM fornecedores")
        data = cursor.fetchall()
        con.close()
        for forn in data:
            self.box_forn.addItem(forn[0])
class config_local(QWidget):
    def __init__(self):
        super().__init__()
        self.config_local = uic.loadUi("templates/interfaces/local_config.ui", self)
        self.box_local = self.findChild(QComboBox, "box_local")
        con = criar_conexao()
        cursor = con.cursor()
        cursor.execute("SELECT nome FROM locais")
        data = cursor.fetchall()
        con.close()
        for local in data:
            self.box_local.addItem(local[0])