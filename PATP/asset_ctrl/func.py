# funcionalidades de cada tela que for chamada

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QFrame,QWidget, QLabel, QGraphicsDropShadowEffect, QAbstractItemView
from PyQt5.QtWidgets import QWidget,QPushButton,QFrame,QLineEdit, QComboBox, QFocusFrame, QScrollArea, QVBoxLayout, QSpinBox, QTableView, QHeaderView
from PyQt5 import uic, QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QResource , QTimer, QLocale
from PyQt5.QtGui import QIcon, QFocusEvent,QDoubleValidator, QStandardItemModel, QStandardItem
from connect import config_acess, config
import mysql.connector # type: ignore

from PyQt5.QtGui import QDoubleValidator, QKeyEvent
from PyQt5.QtCore import Qt


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

        self.search_frame.setGraphicsEffect(self.shadow_user1)
        self.cad_frame.setGraphicsEffect(self.shadow_user2)
        self.info_frame.setGraphicsEffect(self.shadow_user4)



            
    def register(self):
        self.c_frame = self.findChild(QFrame, "createFrame")
        self.u_frame = self.findChild(QFrame, "userFrame")
        self.user_create = uic.loadUi("templates/interfaces/user_create.ui")
        self.c_frame.layout().addWidget(self.user_create)
        self.btn_clear = self.findChild(QPushButton, "btnClear")
        self.btn_clear.clicked.connect(self.clear)
        self.cargo_box = self.findChild(QComboBox, "cargoBox")
        self.cargo_box.setStyleSheet("QComboBox#cargoBox{border: 1px solid #000000;} QComboBox#cargoBox::drop-down{border: 1px solid #000000; border-radius:9px;}")


        self.btn_details = self.findChild(QPushButton, "btn_details")
        self.btn_details.setIcon(alert_circle_svg)
        

        self.shadow_details = QGraphicsDropShadowEffect() 
        self.shadow_details.setOffset(0, 0)
        self.shadow_details.setBlurRadius(9)
        self.shadow_details.setColor(QtGui.QColor(0, 0, 0, 128))
        self.btn_details.setGraphicsEffect(self.shadow_details)

        self.u_frame.hide()
        self.c_frame.show()
        con_cargo = mysql.connector.connect(**config)
        cursor2 = con_cargo.cursor()
        query = "SELECT nome FROM cargo"
        cursor2.execute(query)
        dados = cursor2.fetchall()
        for dado in dados:
            self.cargo_box.addItem(dado[0])
        self.u_frame.hide()
        self.c_frame.show()
        con_cargo.close()
        print('Register')
        


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
        self.btn_add_item = self.findChild(QPushButton, "regItem")
        self.btn_add_item.clicked.connect(self.bag_cad)
        self.produtos = []
        self.produtos_temporarios = []
        
    def bag_cad(self):
        self.cad_itens = bag_item_cad()
        self.cad_frame = self.findChild(QFrame, "cad_frame")
        self.body_frame = self.findChild(QFrame, "body_frame")
        self.cad_frame.layout().addWidget(self.cad_itens)
        self.btn_teste = self.findChild(QPushButton, "test")
        self.body_frame.hide()
        self.cad_frame.show()        
 
    def list_itens(self):
        pass

    def del_item(self, item):
        self.produtos_temporarios.remove(item)
        item.deleteLater()
        self.layout_tb = self.table_item.layout()
        self.layout_tb.removeWidget(item)
        self.layout_tb.update()


class bag_item_cad(QWidget):
    def __init__(self):
        super().__init__()
        
        self.cad_item = uic.loadUi("templates/interfaces/bag_item_cad.ui", self)
        self.name_item = self.findChild(QLineEdit, "name_prod")        
        self.quantidade = self.findChild(QSpinBox, "qnt")
        
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
        
        self.btn_del = self.findChild(QPushButton, "del")
        self.btn_del.clicked.connect(self.deletar_item)

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
        self.atualizar_tabela()

    def temp_list(self):
        nome = self.name_item.text()
        valor = self.number_input.text()
        quantidade = self.quantidade.value()
        if not nome or not valor or quantidade == 0:
            print('Sem valores')
        else:
            self.id_counter += 1
            self.listagem[self.id_counter] = [nome, valor, quantidade]
            self.atualizar_tabela()
            self.clear_c()
        
    def clear_c(self):
        self.name_item.clear()
        self.number_input.clear()
        self.quantidade.clear()
        self.quantidade.setValue(0)

    def atualizar_tabela(self):
        mdl = QStandardItemModel()
        hdr = ["Nome", "Valor", "Quantidade"]
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
            print(f"{self.lista_produtos.model().horizontalHeaderItem(column).text()}: {data}")
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
        con_confirm = mysql.connector.connect(**config)
        cursor = con_confirm.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS teste_produtos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255),
                valor VARCHAR(255)
            )
        ''')
        # Apenas para teste de funcionalidade
        # Faltando regra de negócio
        for item_id, item_data in self.listagem.items():
            nome, valor, quantidade = item_data
            cursor.callproc('cadastra_varios', [nome, valor, quantidade])
            
            '''cursor.execute(''' 
                #INSERT INTO teste_produtos (nome, valor) 
               #VALUES (%s, %s)
            ''', (nome, valor))'''
            
        con_confirm.commit()
        con_confirm.close()
        self.listagem.clear()
        self.atualizar_tabela()
        print("Itens confirmados e adicionados ao banco de dados:", self.listagem)