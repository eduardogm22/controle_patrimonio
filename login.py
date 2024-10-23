# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import resource_rc


class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(1874, 1038)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/imagens/logo__ideau.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        login.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(login)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_verdeescuro = QtWidgets.QFrame(self.centralwidget)
        self.frame_verdeescuro.setMaximumSize(QtCore.QSize(3445, 3445))
        self.frame_verdeescuro.setStyleSheet("background-color : rgb(0, 191, 99)")
        self.frame_verdeescuro.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_verdeescuro.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_verdeescuro.setObjectName("frame_verdeescuro")
        self.imagem_ideau = QtWidgets.QLabel(self.frame_verdeescuro)
        self.imagem_ideau.setGeometry(QtCore.QRect(130, 210, 561, 541))
        self.imagem_ideau.setStyleSheet("")
        self.imagem_ideau.setText("")
        self.imagem_ideau.setPixmap(QtGui.QPixmap(":/newPrefix/imagens/logo__ideau.png"))
        self.imagem_ideau.setScaledContents(True)
        self.imagem_ideau.setObjectName("imagem_ideau")
        self.ButtonEnter_2 = QtWidgets.QPushButton(self.frame_verdeescuro)
        self.ButtonEnter_2.setGeometry(QtCore.QRect(270, 750, 271, 81))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButtonEnter_2.sizePolicy().hasHeightForWidth())
        self.ButtonEnter_2.setSizePolicy(sizePolicy)
        self.ButtonEnter_2.setMinimumSize(QtCore.QSize(171, 0))
        self.ButtonEnter_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtonEnter_2.setMouseTracking(True)
        self.ButtonEnter_2.setTabletTracking(False)
        self.ButtonEnter_2.setStyleSheet("QPushButton { color:rgb(254, 253, 247);\n"
"    border-radius:35px;        \n"
"    border: 4px solid rgb(255, 255, 255);\n"
"    font-size:35px;\n"
" }\n"
"\n"
"QPushButton:hover{background-color:#057A3A;color:white}\n"
"\n"
"QPushButton:pressed{\n"
" padding-left: 5px;\n"
" padding-top:5px;\n"
" \n"
"    background-color: rgb(0, 85, 0);\n"
" \n"
"}\n"
"")
        self.ButtonEnter_2.setCheckable(False)
        self.ButtonEnter_2.setObjectName("ButtonEnter_2")
        self.frame_verde_ecuro = QtWidgets.QFrame(self.frame_verdeescuro)
        self.frame_verde_ecuro.setGeometry(QtCore.QRect(810, 0, 150, 1081))
        self.frame_verde_ecuro.setMaximumSize(QtCore.QSize(150, 1000000))
        self.frame_verde_ecuro.setStyleSheet("background-color: #057A3A")
        self.frame_verde_ecuro.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_verde_ecuro.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_verde_ecuro.setObjectName("frame_verde_ecuro")
        self.horizontalLayout.addWidget(self.frame_verdeescuro)
        self.frame_branco = QtWidgets.QFrame(self.centralwidget)
        self.frame_branco.setMaximumSize(QtCore.QSize(45900, 459000))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.frame_branco.setFont(font)
        self.frame_branco.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.frame_branco.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_branco.setStyleSheet("background-color : rgb(255, 248, 248)")
        self.frame_branco.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_branco.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_branco.setObjectName("frame_branco")
        self.lineEdit_senha = QtWidgets.QLineEdit(self.frame_branco)
        self.lineEdit_senha.setGeometry(QtCore.QRect(290, 550, 441, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEdit_senha.setFont(font)
        self.lineEdit_senha.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lineEdit_senha.setStyleSheet("QLineEdit{\n"
"background-color:#E1DCDB;\n"
"border-radius: 0px;\n"
"padding:15px;\n"
"border-bottom: 2px solid rgb(108, 108, 108);\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover{background-color:rgb(238, 234, 233);color:rgb(181, 178, 177)}")
        self.lineEdit_senha.setObjectName("lineEdit_senha")
        self.lineEdit_email = QtWidgets.QLineEdit(self.frame_branco)
        self.lineEdit_email.setGeometry(QtCore.QRect(310, 640, 391, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEdit_email.setFont(font)
        self.lineEdit_email.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lineEdit_email.setStyleSheet("QLineEdit{\n"
"background-color:#E1DCDB;\n"
"border-radius: 0px;\n"
"padding:15px;\n"
"border-bottom: 2px solid rgb(108, 108, 108);\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover{background-color:rgb(238, 234, 233);color:rgb(181, 178, 177)}")
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.icon_carta_do_email = QtWidgets.QFrame(self.frame_branco)
        self.icon_carta_do_email.setGeometry(QtCore.QRect(250, 640, 71, 71))
        self.icon_carta_do_email.setStyleSheet("QFrame{background-color:#E1DCDB;\n"
"\n"
"}")
        self.icon_carta_do_email.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.icon_carta_do_email.setFrameShadow(QtWidgets.QFrame.Raised)
        self.icon_carta_do_email.setObjectName("icon_carta_do_email")
        self.label_3 = QtWidgets.QLabel(self.icon_carta_do_email)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 51, 41))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/newPrefix/imagens/email.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.lineEdit_user = QtWidgets.QLineEdit(self.frame_branco)
        self.lineEdit_user.setGeometry(QtCore.QRect(290, 370, 441, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEdit_user.setFont(font)
        self.lineEdit_user.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lineEdit_user.setStyleSheet("QLineEdit{\n"
"background-color:#E1DCDB;\n"
"border-radius: 0px;\n"
"padding:15px;\n"
"border-bottom: 2px solid rgb(108, 108, 108);\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover{background-color:rgb(238, 234, 233);color:rgb(181, 178, 177)}")
        self.lineEdit_user.setText("")
        self.lineEdit_user.setObjectName("lineEdit_user")
        self.ControlePatrimonio = QtWidgets.QLabel(self.frame_branco)
        self.ControlePatrimonio.setGeometry(QtCore.QRect(220, 170, 531, 81))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.ControlePatrimonio.setFont(font)
        self.ControlePatrimonio.setStyleSheet("QLabel{\n"
"color:rgb(139, 136, 136)\n"
"}")
        self.ControlePatrimonio.setObjectName("ControlePatrimonio")
        self.CrieUmaConta = QtWidgets.QLabel(self.frame_branco)
        self.CrieUmaConta.setGeometry(QtCore.QRect(330, 310, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.CrieUmaConta.setFont(font)
        self.CrieUmaConta.setStyleSheet("QLabel{\n"
"color:rgb(115, 115, 115)\n"
"}")
        self.CrieUmaConta.setObjectName("CrieUmaConta")
        self.lineEdit_nome_2 = QtWidgets.QLineEdit(self.frame_branco)
        self.lineEdit_nome_2.setGeometry(QtCore.QRect(290, 460, 441, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEdit_nome_2.setFont(font)
        self.lineEdit_nome_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lineEdit_nome_2.setStyleSheet("QLineEdit{\n"
"background-color:#E1DCDB;\n"
"border-radius: 0px;\n"
"padding:15px;\n"
"border-bottom: 2px solid rgb(108, 108, 108);\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover{background-color:rgb(238, 234, 233);color:rgb(181, 178, 177)}")
        self.lineEdit_nome_2.setObjectName("lineEdit_nome_2")
        self.comboBox = QtWidgets.QComboBox(self.frame_branco)
        self.comboBox.setGeometry(QtCore.QRect(250, 750, 451, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.comboBox.setFont(font)
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox.setStyleSheet("background-color:#E1DCDB;\n"
"border-radius: 0px;\n"
"padding:15px;")
        self.comboBox.setObjectName("comboBox")
        self.Nome_4 = QtWidgets.QFrame(self.frame_branco)
        self.Nome_4.setGeometry(QtCore.QRect(230, 460, 71, 71))
        self.Nome_4.setStyleSheet("QFrame{background-color:#E1DCDB;\n"
"\n"
"}")
        self.Nome_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Nome_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Nome_4.setObjectName("Nome_4")
        self.label_icon_nome_5 = QtWidgets.QLabel(self.Nome_4)
        self.label_icon_nome_5.setGeometry(QtCore.QRect(10, 10, 51, 51))
        self.label_icon_nome_5.setText("")
        self.label_icon_nome_5.setPixmap(QtGui.QPixmap(":/newPrefix/imagens/ico.perfil.png"))
        self.label_icon_nome_5.setScaledContents(True)
        self.label_icon_nome_5.setObjectName("label_icon_nome_5")
        self.icon_cadeado_da_senha_2 = QtWidgets.QFrame(self.frame_branco)
        self.icon_cadeado_da_senha_2.setGeometry(QtCore.QRect(230, 550, 71, 71))
        self.icon_cadeado_da_senha_2.setStyleSheet("QFrame{background-color:#E1DCDB;\n"
"}")
        self.icon_cadeado_da_senha_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.icon_cadeado_da_senha_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.icon_cadeado_da_senha_2.setObjectName("icon_cadeado_da_senha_2")
        self.label_4 = QtWidgets.QLabel(self.icon_cadeado_da_senha_2)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 41, 51))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/newPrefix/imagens/senha_icon.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.Button_do_cadastro = QtWidgets.QPushButton(self.frame_branco)
        self.Button_do_cadastro.setGeometry(QtCore.QRect(360, 850, 261, 81))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_do_cadastro.sizePolicy().hasHeightForWidth())
        self.Button_do_cadastro.setSizePolicy(sizePolicy)
        self.Button_do_cadastro.setMinimumSize(QtCore.QSize(171, 0))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Button_do_cadastro.setFont(font)
        self.Button_do_cadastro.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button_do_cadastro.setMouseTracking(True)
        self.Button_do_cadastro.setTabletTracking(False)
        self.Button_do_cadastro.setStyleSheet("\n"
"\n"
"QPushButton { color: rgb(243, 239, 238);\n"
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
" \n"
"}\n"
"")
        self.Button_do_cadastro.setCheckable(False)
        self.Button_do_cadastro.setObjectName("Button_do_cadastro")
        self.label_5 = QtWidgets.QLabel(self.frame_branco)
        self.label_5.setGeometry(QtCore.QRect(260, 720, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(75, 75, 75);")
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(self.frame_branco)
        self.label.setGeometry(QtCore.QRect(360, 830, 251, 20))
        self.label.setStyleSheet("QLabel{\n"
"color:rgb(254, 253, 247);\n"
"}")
        self.label.setObjectName("label")
        self.Nome_3 = QtWidgets.QFrame(self.frame_branco)
        self.Nome_3.setGeometry(QtCore.QRect(230, 370, 71, 71))
        self.Nome_3.setStyleSheet("QFrame{background-color:#E1DCDB;\n"
"\n"
"}")
        self.Nome_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Nome_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Nome_3.setObjectName("Nome_3")
        self.label_icon_nome_3 = QtWidgets.QLabel(self.Nome_3)
        self.label_icon_nome_3.setGeometry(QtCore.QRect(10, 10, 51, 51))
        self.label_icon_nome_3.setText("")
        self.label_icon_nome_3.setPixmap(QtGui.QPixmap(":/newPrefix/imagens/ico.perfil.png"))
        self.label_icon_nome_3.setScaledContents(True)
        self.label_icon_nome_3.setObjectName("label_icon_nome_3")
        self.horizontalLayout.addWidget(self.frame_branco)
        login.setCentralWidget(self.centralwidget)

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "Controle de Patrimônio - Ideau"))
        self.ButtonEnter_2.setWhatsThis(_translate("login", "<html><head/><body><p align=\"center\"><span style=\" font-size:12\n"
"pt;\">Enter</span></p></body></html>"))
        self.ButtonEnter_2.setText(_translate("login", "Entrar"))
        self.lineEdit_senha.setPlaceholderText(_translate("login", "Senha"))
        self.lineEdit_email.setPlaceholderText(_translate("login", "E-mail"))
        self.lineEdit_user.setPlaceholderText(_translate("login", "User"))
        self.ControlePatrimonio.setText(_translate("login", "Controle de Patrimônio"))
        self.CrieUmaConta.setText(_translate("login", "<html><head/><body><p align=\"center\">Crie uma Conta</p></body></html>"))
        self.lineEdit_nome_2.setPlaceholderText(_translate("login", "Nome"))
        self.Button_do_cadastro.setWhatsThis(_translate("login", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Enter</span></p></body></html>"))
        self.Button_do_cadastro.setText(_translate("login", "Inscreva-se"))
        self.label_5.setText(_translate("login", "Cargo:"))
        self.label.setText(_translate("login", "<html><head/><body><p align=\"center\">não tem uma conta? inscreva-se</p></body></html>"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = QtWidgets.QMainWindow()
    ui = Ui_login()
    ui.setupUi(login)
    login.show()
    sys.exit(app.exec_())