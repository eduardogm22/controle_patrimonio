import sys
from PyQt5 import uic, QtWidgets, QtCore, QtGui
from templates.interfaces import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QFrame,QWidget, QLabel, QGraphicsDropShadowEffect, QListWidget, QTableWidget, QListView,QTableView, QAbstractItemView, QHeaderView
from func import user_menu, user_info, bag_view, items_view, rel_view, patr_view, logs_view, config_view, local_info, categ_view
from connect import config, config_acess, criar_conexao
from PyQt5.QtCore import QResource , QTimer, Qt
from PyQt5.QtGui import QIcon, QStandardItemModel, QStandardItem, QFont
import mysql.connector # type: ignore
import os, json
import webbrowser

data_user = ''
data_pass = ''
data_cargo = 15
if os.path.exists('line/dados.json'):
    print("Arquivo JSON existe.")
    v_j = json.load(open("line/dados.json"))
    data_user = v_j["user"]
    data_pass = v_j["password"]
    data_cargo = v_j["cargo"]
    print('Usuário:', data_user, 'Senha:', data_pass, 'Cargo:', data_cargo,'run')
    os.remove('line/dados.json')
else:
    print("Arquivo JSON inexistente run.")

# icones svg
QResource.registerResource("feather/resource.qrc")
home_svg = QIcon("feather/home.svg")
chevrons_left_svg = QIcon("feather/chevrons-left.svg")
menu_svg = QIcon("feather/menu.svg")
user_svg = QIcon("feather/user.svg")
codesandbox_svg = QIcon("feather-black/codesandbox.svg")
database_svg = QIcon("feather-black/database.svg")
map_pin_svg = QIcon("feather-black/map-pin.svg")
dollar_sign_svg = QIcon("feather-black/dollar-sign.svg")
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



class interface(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('templates/interfaces/interface.ui', self)
        self.label_user = self.findChild(QLabel, "labelUser")
        self.label_user.setText(user)
        self.ui.setWindowIcon(server_svg)


        # botoes da barra de menu
        self.btn_rel = self.findChild(QPushButton, "relBtn")
        self.btn_rel.setIcon(file_text_svg)
        self.btn_rel.installEventFilter(self)     
        self.btn_rel.clicked.connect(self.rel_screen)  

        self.btn_users = self.findChild(QPushButton, "usersBtn")
        self.btn_users.setIcon(users_svg)
        self.btn_users.installEventFilter(self)        

        self.btn_bag = self.findChild(QPushButton, "bagBtn")
        self.btn_bag.setIcon(shopping_bag)
        self.btn_bag.installEventFilter(self)        

        self.btn_logs = self.findChild(QPushButton, "logBtn")
        self.btn_logs.setIcon(activity_svg)
        self.btn_logs.installEventFilter(self)
        self.btn_logs.clicked.connect(self.config_screen)  

        self.btn_bckp = self.findChild(QPushButton, "bckpBtn")
        self.btn_bckp.setIcon(save_svg)
        self.btn_bckp.installEventFilter(self)

        self.btn_help = self.findChild(QPushButton, "helpBtn")
        self.btn_help.setIcon(help_circle_svg)
        self.btn_help.installEventFilter(self)
        self.btn_help.clicked.connect(self.help_screen)

        self.btn_doc = self.findChild(QPushButton, "docBtn")
        self.btn_doc.setIcon(link_svg)
        self.btn_doc.installEventFilter(self)
        
        # TESTE TEXTO PRODUTO
        self.text_item = self.findChild(QLabel, "textProd")
        con = criar_conexao()
        cursor = con.cursor()
        cursor.execute('select count(*) from patrimonios')
        data_prod = cursor.fetchall()
        self.text_item.setText('Quantidade: '+str(data_prod[0][0]))
        con.close()
        
        self.text_logs = self.findChild(QLabel, "textLogs")
        self.text_logs.setText('Logs')

        self.text_local = self.findChild(QLabel, "textLocal")
        self.text_local.setText('Local')

        self.text_vp = self.findChild(QLabel, "textVp")
        con = criar_conexao()
        cursor = con.cursor()
        cursor.execute('select sum(valor_unitario) from patrimonios')
        data_vp = cursor.fetchall()
        self.text_vp.setText('R$: '+str(data_vp[0][0]))
        con.close()
        

        # instância das sombras 
        self.shadow_frame1 = QGraphicsDropShadowEffect() 
        self.shadow_frame1.setOffset(0, 0)  # posição da sombra
        self.shadow_frame1.setBlurRadius(9)  # tamanho da sombra
        self.shadow_frame1.setColor(QtGui.QColor(0, 100, 0, 128))

        self.shadow_frame2 = QGraphicsDropShadowEffect() 
        self.shadow_frame2.setOffset(0, 0)
        self.shadow_frame2.setBlurRadius(9)
        self.shadow_frame2.setColor(QtGui.QColor(0, 0, 0, 128))

        self.shadow_frame3 = QGraphicsDropShadowEffect() 
        self.shadow_frame3.setOffset(0, 0)
        self.shadow_frame3.setBlurRadius(9)
        self.shadow_frame3.setColor(QtGui.QColor(0, 0, 0, 128))

        self.shadow_frame4 = QGraphicsDropShadowEffect() 
        self.shadow_frame4.setOffset(0, 0)
        self.shadow_frame4.setBlurRadius(9)
        self.shadow_frame4.setColor(QtGui.QColor(0, 0, 0, 128))
        
        self.shadow_rel = QGraphicsDropShadowEffect() 
        self.shadow_rel.setOffset(0, 0)
        self.shadow_rel.setBlurRadius(9)
        self.shadow_rel.setColor(QtGui.QColor(0, 0, 0, 128))
        
        self.shadow_logs = QGraphicsDropShadowEffect() 
        self.shadow_logs.setOffset(0, 0)
        self.shadow_logs.setBlurRadius(9)
        self.shadow_logs.setColor(QtGui.QColor(0, 0, 0, 128))

        self.shadow_menu = QGraphicsDropShadowEffect() 
        self.shadow_menu.setOffset(0, 0)
        self.shadow_menu.setBlurRadius(9)   
        self.shadow_menu.setColor(QtGui.QColor(0, 0, 0, 128))   

        # BANCO TESTE
        self.table_view = self.findChild(QTableView, "tableView")
        conn = mysql.connector.connect(**config) # argumentos do dicionário config...
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuario_nome_view")
        results = cursor.fetchall()

         # Criar o modelo para o QTableView
        model = QStandardItemModel(len(results), 3)  # (número de linhas, número de colunas)

        for row_idx, row_data in enumerate(results):
            for col_idx, data in enumerate(row_data):
                item = QStandardItem(str(data))
                item.setFont(QFont("Roboto", 12))
                item.setTextAlignment(Qt.AlignCenter)
                model.setHorizontalHeaderLabels(['ID', 'Usuario', 'Email'])
                model.setItem(row_idx, col_idx, item)


        header = self.table_view.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        header.setStretchLastSection(True)
        self.table_view.setModel(model)
        self.table_view.setGridStyle(Qt.NoPen)
        #self.table_view.setHorizontalHeader(None)
        self.table_view.setAlternatingRowColors(True)
        self.table_view.setStyleSheet("alternate-background-color: #F0F0F0; background-color: #FFFFFF;")
        self.table_view.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_view.setEditTriggers(QAbstractItemView.NoEditTriggers)
        
        conn.close()

        self.table_view2 = self.findChild(QTableView, "tableView_2")
        conn2 = mysql.connector.connect(**config) # argumentos do dicionário config...
        cursor = conn2.cursor()
        cursor.execute("SELECT idpessoa, usuario FROM usuarios")
            # teste 1
        results1 = cursor.fetchall()
        for row in results1:
            nome, id = row



         # Criar o modelo para o QTableView
        model2 = QStandardItemModel(len(results1), 2)  # (número de linhas, número de colunas)
        for row_idx, row_data in enumerate(results1):
            for col_idx, data in enumerate(row_data):
                item = QStandardItem(str(data))
                item.setFont(QFont("Roboto", 12))
                item.setTextAlignment(Qt.AlignCenter)
                model2.setItem(row_idx, col_idx, item)
        header2 = self.table_view2.horizontalHeader()
        header2.setSectionResizeMode(QHeaderView.Stretch)
        header2.setStretchLastSection(True)
        self.table_view2.setModel(model2)
        self.table_view2.setGridStyle(Qt.NoPen)
        self.table_view2.setAlternatingRowColors(True)
        self.table_view2.setStyleSheet("alternate-background-color: #F0F0F0; background-color: #FFFFFF;")
        self.table_view2.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_view2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        conn.close()




        # botões e icones header
        self.btn_account = self.findChild(QPushButton, "accountBtn")


        self.btn_account.setToolTip("Conta") # <- vai ser usado para auxiliar o usuário com balões de informação, no momento apenas no botão conta para teste.



        self.btn_account.setIcon(user_svg)
        self.btn_account.installEventFilter(self)

        self.btn_home = self.findChild(QWidget, "btnHome")
        self.home_btn = self.findChild(QPushButton, "homeBtn")
        self.home_btn.setIcon(home_svg)
        self.btn_home.hide() 
        self.home_btn.clicked.connect(self.home)
        self.btn_home.installEventFilter(self)
        # botão home | só aparece quando outra tela estiver aberta
        # botoes da home

        self.btn_details_reg = self.findChild(QPushButton, 'btnRegDetails')
        self.btn_details_reg.setIcon(alert_circle_svg)
        self.btn_details_log = self.findChild(QPushButton, 'btnLogDetails')
        self.btn_details_log.setIcon(alert_circle_svg)


        # instancia installEventFilter para aplicação de eventos
        # o nome do objeto é diferente do identificador usado no css
        # o identificador do css precisa ser adicionado direto no código.
        self.btn_item = self.findChild(QPushButton, "btnItem")
        self.btn_item.setIcon(codesandbox_svg)
        self.frame_card1 = self.findChild(QFrame, 'card1') 
        self.frame_card1.setObjectName("frame_card1") 
        self.btn_item.installEventFilter(self)
        self.btn_item.clicked.connect(self.item_view)

        self.btn_reg = self.findChild(QPushButton, "btnReg")
        self.btn_reg.setIcon(database_svg)
        self.frame_card2 = self.findChild(QFrame, 'card2')
        self.frame_card2.setObjectName("frame_card2")
        self.btn_reg.installEventFilter(self)
        self.btn_reg.clicked.connect(self.logs_screen)

        self.btn_local = self.findChild(QPushButton, "btnLocal")
        self.btn_local.setIcon(map_pin_svg)
        self.frame_card3 = self.findChild(QFrame, 'card3')
        self.frame_card3.setObjectName("frame_card3")
        self.btn_local.installEventFilter(self)
        self.btn_local.clicked.connect(self.local_screen)

        self.btn_vp = self.findChild(QPushButton, "btnVP")
        self.btn_vp.setIcon(dollar_sign_svg)
        self.frame_card4 = self.findChild(QFrame, 'card4')
        self.frame_card4.setObjectName("frame_card4")
        self.btn_vp.installEventFilter(self)
        self.btn_vp.clicked.connect(self.patr_screen)



        # botões do menu lateral que chamam as interfaces das classes externas
        self.btn_users_menu = self.findChild(QPushButton, "usersBtn")
        self.btn_account.clicked.connect(self.menu_info_user)
        self.btn_users_menu.clicked.connect(self.menu_users)
        self.btn_bag.clicked.connect(self.bag_screen)        


        # efeito de sombra aplicado aos frames
        self.frame_card1.setGraphicsEffect(self.shadow_frame1)
        self.frame_card2.setGraphicsEffect(self.shadow_frame2)
        self.frame_card3.setGraphicsEffect(self.shadow_frame3)
        self.frame_card4.setGraphicsEffect(self.shadow_frame4)


        self.h_frame2 = self.findChild(QFrame, 'h_frame2')
        self.h_frame2.setGraphicsEffect(self.shadow_rel)
        self.h_frame1 = self.findChild(QFrame, 'h_frame1')
        self.h_frame1.setGraphicsEffect(self.shadow_logs)

        self.table_view.clicked.connect(self.handle_row_click)
        self.selected_rows = []

        self.show()


    def handle_row_click(self, index):
        row = index.row()
        print(f"Dados da linha {row}:")
        for column in range(self.table_view.model().columnCount()):
            data = self.table_view.model().index(row, column).data()
            print(f"{self.table_view.model().horizontalHeaderItem(column).text()}: {data}")
        self.selected_rows.clear()
        self.selected_rows.append(self.table_view.model().index(row, column).data())
        print(self.selected_rows)




    # Função para aplicação do efeito hover e sombra no CSS
    # Faltando testes, nem todas as utilizades do CSS são aceitas pelo Qt
    def eventFilter(self, obj, event):

        # botão produtos
        if obj == self.btn_item:
            if event.type() == QtCore.QEvent.Leave:
                self.frame_card1.setStyleSheet("QFrame#frame_card1{border:1px solid #057A3A;}")
            elif event.type() == QtCore.QEvent.Enter:
                self.frame_card1.setStyleSheet("QFrame#frame_card1{border:2px solid #057A3A;border-radius:15px;}")

        # botão logs
        elif obj == self.btn_reg:
            if event.type() == QtCore.QEvent.Leave:
                self.frame_card2.setStyleSheet("QFrame#frame_card2{border: 1px solid #057A3A;}")
            elif event.type() == QtCore.QEvent.Enter:
                self.frame_card2.setStyleSheet("QFrame#frame_card2{border:2px solid #057A3A;border-radius:15px;}")

        # botão local       
        elif obj == self.btn_local:
            if event.type() == QtCore.QEvent.Leave:
                self.frame_card3.setStyleSheet("QFrame#frame_card3{border: 1px solid #057A3A;}")
            elif event.type() == QtCore.QEvent.Enter:
                self.frame_card3.setStyleSheet("QFrame#frame_card3{border:2px solid #057A3A;border-radius:15px;}")

        # botão patrimônio
        elif obj == self.btn_vp:
            if event.type() == QtCore.QEvent.Leave:
                self.frame_card4.setStyleSheet("QFrame#frame_card4{border: 1px solid #057A3A;}")
            elif event.type() == QtCore.QEvent.Enter:
                self.frame_card4.setStyleSheet("QFrame#frame_card4{border:2px solid #057A3A;border-radius:15px;}")

        # botão conta
        elif obj == self.btn_account:
            if event.type() == QtCore.QEvent.Enter:
                shadow = QGraphicsDropShadowEffect()
                shadow.setOffset(0, 0)
                shadow.setBlurRadius(3)
                shadow.setColor(QtGui.QColor(0, 0, 2))
                self.btn_account.setGraphicsEffect(shadow)
            elif event.type() == QtCore.QEvent.Leave:
                self.btn_account.setGraphicsEffect(None)
        
        # botão home
        elif obj == self.btn_home:
            if event.type() == QtCore.QEvent.Enter:
                shadow = QGraphicsDropShadowEffect()
                shadow.setOffset(0, 0)
                shadow.setBlurRadius(3)
                shadow.setColor(QtGui.QColor(0, 0, 2))
                self.home_btn.setGraphicsEffect(shadow)
            elif event.type() == QtCore.QEvent.Leave:
                self.home_btn.setGraphicsEffect(None)
    
        # botões menu lateral
        elif obj == self.btn_rel:
            if event.type() == QtCore.QEvent.Enter:
                shadow = QGraphicsDropShadowEffect()
                shadow.setOffset(0, 0)
                shadow.setBlurRadius(0.3)
                shadow.setColor(QtGui.QColor(0, 0, 1))
                self.btn_rel.setGraphicsEffect(shadow)
            elif event.type() == QtCore.QEvent.Leave:
                self.btn_rel.setGraphicsEffect(None)

        elif obj == self.btn_users:
            if event.type() == QtCore.QEvent.Enter:
                shadow = QGraphicsDropShadowEffect()
                shadow.setOffset(0, 0)
                shadow.setBlurRadius(0.3)
                shadow.setColor(QtGui.QColor(0, 0, 1))
                self.btn_users.setGraphicsEffect(shadow)
            elif event.type() == QtCore.QEvent.Leave:
                self.btn_users.setGraphicsEffect(None)

        elif obj == self.btn_bag:
            if event.type() == QtCore.QEvent.Enter:
                shadow = QGraphicsDropShadowEffect()
                shadow.setOffset(0, 0)
                shadow.setBlurRadius(0.3)
                shadow.setColor(QtGui.QColor(0, 0, 1))
                self.btn_bag.setGraphicsEffect(shadow)
            elif event.type() == QtCore.QEvent.Leave:
                self.btn_bag.setGraphicsEffect(None)

        elif obj == self.btn_logs:
            if event.type() == QtCore.QEvent.Enter:
                shadow = QGraphicsDropShadowEffect()
                shadow.setOffset(0, 0)
                shadow.setBlurRadius(0.3)
                shadow.setColor(QtGui.QColor(0, 0, 1))
                self.btn_logs.setGraphicsEffect(shadow)
            elif event.type() == QtCore.QEvent.Leave:
                self.btn_logs.setGraphicsEffect(None)

        elif obj == self.btn_bckp:
            if event.type() == QtCore.QEvent.Enter:
                shadow = QGraphicsDropShadowEffect()
                shadow.setOffset(0, 0)
                shadow.setBlurRadius(0.3)
                shadow.setColor(QtGui.QColor(0, 0, 1))
                self.btn_bckp.setGraphicsEffect(shadow)
            elif event.type() == QtCore.QEvent.Leave:
                self.btn_bckp.setGraphicsEffect(None)

        elif obj == self.btn_help:
            if event.type() == QtCore.QEvent.Enter:
                shadow = QGraphicsDropShadowEffect()
                shadow.setOffset(0, 0)
                shadow.setBlurRadius(0.3)
                shadow.setColor(QtGui.QColor(0, 0, 1))
                self.btn_help.setGraphicsEffect(shadow)
            elif event.type() == QtCore.QEvent.Leave:
                self.btn_help.setGraphicsEffect(None)

        elif obj == self.btn_doc:
            if event.type() == QtCore.QEvent.Enter:
                shadow = QGraphicsDropShadowEffect()
                shadow.setOffset(0, 0)
                shadow.setBlurRadius(0.3)
                shadow.setColor(QtGui.QColor(0, 0, 1))
                self.btn_doc.setGraphicsEffect(shadow)
            elif event.type() == QtCore.QEvent.Leave:
                self.btn_doc.setGraphicsEffect(None)

        return super().eventFilter(obj, event)

    # Função que limpa o QFrame para fazer a atribuição de um QWidget diferente
    def clear_frame(self):
        for widget in self.frame.findChildren(QWidget):
            widget.deleteLater()

    def home(self):
        self.h_frame = self.findChild(QFrame, "homeFrame")
        self.clear_frame()
        self.h_frame.show()
        self.btn_home.hide()

    # Chamada para tela do usuário
    def menu_info_user(self):
        self.frame = self.findChild(QFrame, "userFrame")
        self.h_frame = self.findChild(QFrame, "homeFrame")
        self.user_info = user_info()
        self.clear_frame()
        self.frame.layout().addWidget(self.user_info)
        if self.user_info in self.frame.findChildren(QWidget):
            self.h_frame.hide()
            self.frame.show()
            if self.btn_home.isVisible() == False:
                self.btn_home.show()

    # Chamada para tela de gerenciamento de usuários
    def menu_users(self):
        print('Usuário:', data_user, 'Senha:', data_pass, 'Cargo:', data_cargo)
        self.frame = self.findChild(QFrame, "userFrame")
        self.h_frame = self.findChild(QFrame, "homeFrame")
        self.users_menu = user_menu()
        self.clear_frame()
        self.frame.layout().addWidget(self.users_menu)
        if self.users_menu in self.frame.findChildren(QWidget):
            self.h_frame.hide()
            self.frame.show()
            if self.btn_home.isVisible() == False:
                self.btn_home.show()

    def bag_screen(self):
        self.frame = self.findChild(QFrame, "userFrame")
        self.h_frame = self.findChild(QFrame, "homeFrame")
        self.bag = bag_view()
        self.clear_frame()
        self.frame.layout().addWidget(self.bag)
        if self.bag in self.frame.findChildren(QWidget):
            self.h_frame.hide()
            self.frame.show()
            if self.btn_home.isVisible() == False:
                self.btn_home.show()
                
    def item_view(self):
        self.frame = self.findChild(QFrame, "userFrame")
        self.h_frame = self.findChild(QFrame, "homeFrame")  
        self.itemview = items_view()
        self.clear_frame()
        self.frame.layout().addWidget(self.itemview)
        if self.itemview in self.frame.findChildren(QWidget):
            self.h_frame.hide()
            self.frame.show()
            if self.btn_home.isVisible() == False:
                self.btn_home.show()


    def rel_screen(self):
        self.frame = self.findChild(QFrame, "userFrame")
        self.h_frame = self.findChild(QFrame, "homeFrame")
        self.rel = rel_view()
        self.clear_frame()
        self.frame.layout().addWidget(self.rel)
        if self.rel in self.frame.findChildren(QWidget):
            self.h_frame.hide()
            self.frame.show()
            if self.btn_home.isVisible() == False:
                self.btn_home.show()
                
    def patr_screen(self):
        self.frame = self.findChild(QFrame, "userFrame")
        self.h_frame = self.findChild(QFrame, "homeFrame")
        self.patr = patr_view()
        self.clear_frame()
        self.frame.layout().addWidget(self.patr)
        if self.patr in self.frame.findChildren(QWidget):
            self.h_frame.hide()
            self.frame.show()
            if self.btn_home.isVisible() == False:
                self.btn_home.show()
                
    def logs_screen(self):
        self.frame = self.findChild(QFrame, "userFrame")
        self.h_frame = self.findChild(QFrame, "homeFrame")
        self.logs = logs_view()
        self.clear_frame()
        self.frame.layout().addWidget(self.logs)
        if self.logs in self.frame.findChildren(QWidget):
            self.h_frame.hide()
            self.frame.show()
            if self.btn_home.isVisible() == False:
                self.btn_home.show()
                
    def config_screen(self):
        print('teste config')
        self.frame = self.findChild(QFrame, "userFrame")
        self.h_frame = self.findChild(QFrame, "homeFrame")
        self.config = config_view()
        self.clear_frame()
        self.frame.layout().addWidget(self.config)
        if self.config in self.frame.findChildren(QWidget):
            self.h_frame.hide()
            self.frame.show()
            if self.btn_home.isVisible() == False:
                self.btn_home.show()
    def local_screen(self):
        self.frame = self.findChild(QFrame, "userFrame")
        self.h_frame = self.findChild(QFrame, "homeFrame")
        self.local = local_info()
        self.clear_frame()
        self.frame.layout().addWidget(self.local)
        if self.local in self.frame.findChildren(QWidget):
            self.h_frame.hide()
            self.frame.show()
            if self.btn_home.isVisible() == False:
                self.btn_home.show()


    # pagina de ajuda e documentação
    def help_screen(self):
        help_page= os.path.abspath("asset_ctrl/documentation/helps/index.html")
        webbrowser.open(f"file://{help_page}")

# contexto
if __name__ == "__main__":    
    app = QApplication(sys.argv)
    if len(sys.argv) > 1:
        user = sys.argv[1]
        window = interface()
        window.show()
        sys.exit(app.exec_())
    else:
        user = "Desconhecido"