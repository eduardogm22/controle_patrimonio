from PyQt5 import QtCore, QtGui, QtWidgets
from imagem import resource_rc # remocao de borda e tela transparente da linha 12 e 13
#adicionei borda com  desfoque da linha 27 à 31

class Ui_tlentrar(object):
    def setupUi(self, tlentrar):
        tlentrar.setObjectName("tlentrar")
        tlentrar.resize(950, 764)
        tlentrar.setWindowFlags(QtCore.Qt.FramelessWindowHint) # tira borda
        tlentrar.setAttribute(QtCore.Qt.WA_TranslucentBackground) # deixa a tela transparente
        font = QtGui.QFont()
        font.setPointSize(7)
        tlentrar.setFont(font)
        self.centralwidget = QtWidgets.QWidget(tlentrar)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(60, 30, 841, 781))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(210, 50, 421, 641))
        self.label.setStyleSheet("background-color : rgb(0, 191, 99);\n"
"border-radius: 25px;\n"
"")

        shadow_effect = QtWidgets.QGraphicsDropShadowEffect(self.label)
        shadow_effect.setBlurRadius(100)  # Grau de desfoque
        shadow_effect.setXOffset(0)  # Deslocamento horizontal
        shadow_effect.setYOffset(0)  # Deslocamento vertical
        shadow_effect.setColor(QtGui.QColor(0, 0, 0, 120))  # Cor da sombra com opacidade
        self.label.setGraphicsEffect(shadow_effect)

        self.label.setText("")
        self.label.setObjectName("label")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(220, 260, 401, 391))
        self.widget_2.setStyleSheet("background-color: rgb(232, 232, 232);\n"
"border-radius: 25px\n"
"\n"
"")
        self.widget_2.setObjectName("widget_2")
        self.lineEdit_user_2 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_user_2.setGeometry(QtCore.QRect(90, 60, 281, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEdit_user_2.setFont(font)
        self.lineEdit_user_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lineEdit_user_2.setStyleSheet("QLineEdit{\n"
"background-color:#E1DCDB;\n"
"border-radius: 0px;\n"
"padding:15px;\n"
"border-bottom: 2px solid rgb(108, 108, 108);\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover{background-color:rgb(238, 234, 233);color:rgb(181, 178, 177)}")
        self.lineEdit_user_2.setText("")
        self.lineEdit_user_2.setObjectName("lineEdit_user_2")
        self.lineEdit_senha_2 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_senha_2.setGeometry(QtCore.QRect(90, 140, 281, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEdit_senha_2.setFont(font)
        self.lineEdit_senha_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lineEdit_senha_2.setStyleSheet("QLineEdit{\n"
"background-color:#E1DCDB;\n"
"border-radius: 0px;\n"
"padding:15px;\n"
"border-bottom: 2px solid rgb(108, 108, 108);\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover{background-color:rgb(238, 234, 233);color:rgb(181, 178, 177)}")
        self.lineEdit_senha_2.setObjectName("lineEdit_senha_2")
        self.Nome_5 = QtWidgets.QFrame(self.widget_2)
        self.Nome_5.setGeometry(QtCore.QRect(40, 60, 61, 61))
        self.Nome_5.setStyleSheet("QFrame{background-color:#E1DCDB;\n"
"border-radius: 0px\n"
"}")
        self.Nome_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Nome_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Nome_5.setObjectName("Nome_5")
        self.label_icon_nome_4 = QtWidgets.QLabel(self.Nome_5)
        self.label_icon_nome_4.setGeometry(QtCore.QRect(10, 10, 41, 41))
        self.label_icon_nome_4.setText("")
        self.label_icon_nome_4.setPixmap(QtGui.QPixmap(":/newPrefix/imagens/ico.perfil.png"))
        self.label_icon_nome_4.setScaledContents(True)
        self.label_icon_nome_4.setObjectName("label_icon_nome_4")
        self.icon_cadeado_da_senha_3 = QtWidgets.QFrame(self.widget_2)
        self.icon_cadeado_da_senha_3.setGeometry(QtCore.QRect(40, 140, 61, 61))
        self.icon_cadeado_da_senha_3.setStyleSheet("QFrame{background-color:#E1DCDB;\n"
"border-radius: 0px\n"
"}")
        self.icon_cadeado_da_senha_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.icon_cadeado_da_senha_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.icon_cadeado_da_senha_3.setObjectName("icon_cadeado_da_senha_3")
        self.label_6 = QtWidgets.QLabel(self.icon_cadeado_da_senha_3)
        self.label_6.setGeometry(QtCore.QRect(20, 10, 31, 41))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/newPrefix/imagens/senha_icon.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.Button_entrar = QtWidgets.QPushButton(self.widget_2)
        self.Button_entrar.setGeometry(QtCore.QRect(120, 260, 181, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_entrar.sizePolicy().hasHeightForWidth())
        self.Button_entrar.setSizePolicy(sizePolicy)
        self.Button_entrar.setMinimumSize(QtCore.QSize(171, 0))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Button_entrar.setFont(font)
        self.Button_entrar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button_entrar.setMouseTracking(True)
        self.Button_entrar.setTabletTracking(False)
        self.Button_entrar.setStyleSheet("QPushButton { color: rgb(243, 239, 238);\n"
"    border-radius:35px;        \n"
"    border: 4px solid #00BF63;\n"
"    background-color:#00BF63;\n"
"    font: 18pt \"MS Shell Dlg 2\";\n"
" }\n"
"\n"
"QPushButton:hover{background-color:rgb(255, 240, 238);color:#00BF63}\n"
"\n"
"QPushButton:pressed{\n"
" padding-left: 5px;\n"
" padding-top:5px;\n"
"    background-color: rgb(227, 227, 227);\n"
"}\n"
"\n"
"")
        self.Button_entrar.setCheckable(False)
        self.Button_entrar.setObjectName("Button_entrar")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(320, 60, 211, 191))
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/imagens/logo__ideau.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        tlentrar.setCentralWidget(self.centralwidget)

        self.retranslateUi(tlentrar)
        QtCore.QMetaObject.connectSlotsByName(tlentrar)

    def retranslateUi(self, tlentrar):
        _translate = QtCore.QCoreApplication.translate
        tlentrar.setWindowTitle(_translate("tlentrar", "tlentrar"))
        self.lineEdit_user_2.setPlaceholderText(_translate("tlentrar", "Usuário"))
        self.lineEdit_senha_2.setPlaceholderText(_translate("tlentrar", "Senha"))
        self.Button_entrar.setWhatsThis(_translate("tlentrar", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Enter</span></p></body></html>"))
        self.Button_entrar.setText(_translate("tlentrar", "Entrar"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tlentrar = QtWidgets.QMainWindow()
    ui = Ui_tlentrar()
    ui.setupUi(tlentrar)
    tlentrar.show()
    sys.exit(app.exec_())