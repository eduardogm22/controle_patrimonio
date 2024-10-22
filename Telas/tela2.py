from PyQt5 import QtCore, QtGui, QtWidgets
from imagem import resource_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1908, 1013)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/logo__ideau.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frameVerdeClaro = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.frameVerdeClaro.setFont(font)
        self.frameVerdeClaro.setStyleSheet("background-color: rgb(0, 191, 99);")
        self.frameVerdeClaro.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameVerdeClaro.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameVerdeClaro.setObjectName("frameVerdeClaro")
        self.widget_bagulhoBranco = QtWidgets.QWidget(self.frameVerdeClaro)
        self.widget_bagulhoBranco.setGeometry(QtCore.QRect(20, 320, 1501, 661))
        self.widget_bagulhoBranco.setStyleSheet("background-color: rgb(255, 248, 248);")
        self.widget_bagulhoBranco.setObjectName("widget_bagulhoBranco")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.widget_bagulhoBranco)
        self.verticalScrollBar.setGeometry(QtCore.QRect(1470, 30, 31, 631))
        self.verticalScrollBar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.verticalScrollBar.setStyleSheet("\n"
"background-color: rgb(255, 242, 0);")
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.frame_2faixaAmarela = QtWidgets.QFrame(self.widget_bagulhoBranco)
        self.frame_2faixaAmarela.setGeometry(QtCore.QRect(0, 0, 1501, 31))
        self.frame_2faixaAmarela.setStyleSheet("background-color: rgb(255, 242, 0);")
        self.frame_2faixaAmarela.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2faixaAmarela.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2faixaAmarela.setObjectName("frame_2faixaAmarela")
        self.columnView = QtWidgets.QColumnView(self.frame_2faixaAmarela)
        self.columnView.setGeometry(QtCore.QRect(0, 20, 221, 31))
        self.columnView.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.columnView.setObjectName("columnView")
        self.treeWidget = QtWidgets.QTreeWidget(self.frame_2faixaAmarela)
        self.treeWidget.setGeometry(QtCore.QRect(0, 0, 1471, 671))
        font = QtGui.QFont()
        font.setPointSize(39)
        self.treeWidget.setFont(font)
        self.treeWidget.setStyleSheet(" QHeaderView::section {\n"
"        \n"
"    font: 12pt \"MS Shell Dlg 2\";\n"
"        background-color: rgb(255, 242, 0);  \n"
"        color: black;  \n"
"        font-weight: bold;\n"
"        height: 30px;\n"
"\n"
"    }\n"
"")
        self.treeWidget.setObjectName("treeWidget")
        self.scrollArea = QtWidgets.QScrollArea(self.widget_bagulhoBranco)
        self.scrollArea.setGeometry(QtCore.QRect(-20, 30, 1491, 641))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1489, 639))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.frame_verdeEscuro = QtWidgets.QFrame(self.frameVerdeClaro)
        self.frame_verdeEscuro.setGeometry(QtCore.QRect(-1, 200, 1541, 811))
        self.frame_verdeEscuro.setStyleSheet("background-color: rgb(5, 122, 58);")
        self.frame_verdeEscuro.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_verdeEscuro.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_verdeEscuro.setObjectName("frame_verdeEscuro")
        self.pushButton = QtWidgets.QPushButton(self.frame_verdeEscuro)
        self.pushButton.setGeometry(QtCore.QRect(1250, 20, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{background-color: rgb(255, 242, 0);\n"
"border-radius:12px;\n"
"border: 2px solid black;\n"
"}\n"
"QPushButton:hover{background-color:rgb(223, 223, 111);color:rgb(72, 72, 72)}")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_nome = QtWidgets.QLineEdit(self.frame_verdeEscuro)
        self.lineEdit_nome.setGeometry(QtCore.QRect(640, 30, 591, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_nome.setFont(font)
        self.lineEdit_nome.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit_nome.setStyleSheet("QLineEdit{\n"
"background-color:#E1DCDB;\n"
"border-radius: 3px;\n"
"padding:15px;\n"
"border: 1px solid rgb(129, 129, 129);\n"
"}\n"
"\n"
"QLineEdit:hover{background-color:rgb(238, 234, 233);color:rgb(181, 178, 177)}")
        self.lineEdit_nome.setObjectName("lineEdit_nome")
        self.comboBox = QtWidgets.QComboBox(self.frame_verdeEscuro)
        self.comboBox.setGeometry(QtCore.QRect(20, 30, 461, 51))
        self.comboBox.setStyleSheet("background-color:#E1DCDB;\n"
"color:rgb(121, 121, 121);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"padding:15px;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.icon_ideau = QtWidgets.QLabel(self.frameVerdeClaro)
        self.icon_ideau.setGeometry(QtCore.QRect(30, 0, 211, 201))
        self.icon_ideau.setText("")
        self.icon_ideau.setPixmap(QtGui.QPixmap(":/newPrefix/logo__ideau.png"))
        self.icon_ideau.setScaledContents(True)
        self.icon_ideau.setObjectName("icon_ideau")
        self.pushButton_NOVO = QtWidgets.QPushButton(self.frameVerdeClaro)
        self.pushButton_NOVO.setGeometry(QtCore.QRect(1610, 200, 241, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_NOVO.setFont(font)
        self.pushButton_NOVO.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_NOVO.setStyleSheet("QPushButton{background-color:rgb(5, 122, 58);\n"
"color: rgb(243, 239, 238);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"} \n"
"QPushButton:hover{background-color:white ;color:rgb(5, 122, 58); border-color: rgb(5, 122, 58);}\n"
"")
        self.pushButton_NOVO.setObjectName("pushButton_NOVO")
        self.pushButton_EXCLUIR = QtWidgets.QPushButton(self.frameVerdeClaro)
        self.pushButton_EXCLUIR.setGeometry(QtCore.QRect(1610, 320, 241, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_EXCLUIR.setFont(font)
        self.pushButton_EXCLUIR.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_EXCLUIR.setStyleSheet("QPushButton{background-color:rgb(5, 122, 58);\n"
"color: rgb(243, 239, 238);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"} \n"
"QPushButton:hover{background-color:white ;color:rgb(5, 122, 58); border-color: rgb(5, 122, 58);}\n"
"")
        self.pushButton_EXCLUIR.setObjectName("pushButton_EXCLUIR")
        self.pushButton_FILTRO = QtWidgets.QPushButton(self.frameVerdeClaro)
        self.pushButton_FILTRO.setGeometry(QtCore.QRect(1610, 440, 241, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_FILTRO.setFont(font)
        self.pushButton_FILTRO.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_FILTRO.setStyleSheet("QPushButton{background-color:rgb(5, 122, 58);\n"
"color: rgb(243, 239, 238);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"} \n"
"QPushButton:hover{background-color:white ;color:rgb(5, 122, 58); border-color: rgb(5, 122, 58);}\n"
"")
        self.pushButton_FILTRO.setObjectName("pushButton_FILTRO")
        self.pushButton_RELATORIO = QtWidgets.QPushButton(self.frameVerdeClaro)
        self.pushButton_RELATORIO.setGeometry(QtCore.QRect(1610, 560, 241, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_RELATORIO.setFont(font)
        self.pushButton_RELATORIO.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_RELATORIO.setStyleSheet("QPushButton{background-color:rgb(5, 122, 58);\n"
"color: rgb(243, 239, 238);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"} \n"
"QPushButton:hover{background-color:white ;color:rgb(5, 122, 58); border-color: rgb(5, 122, 58);}\n"
"")
        self.pushButton_RELATORIO.setObjectName("pushButton_RELATORIO")
        self.pushButton_RELATORIO_2 = QtWidgets.QPushButton(self.frameVerdeClaro)
        self.pushButton_RELATORIO_2.setGeometry(QtCore.QRect(1610, 680, 241, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_RELATORIO_2.setFont(font)
        self.pushButton_RELATORIO_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_RELATORIO_2.setStyleSheet("QPushButton{background-color:rgb(5, 122, 58);\n"
"color: rgb(243, 239, 238);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"} \n"
"QPushButton:hover{background-color:white ;color:rgb(5, 122, 58); border-color: rgb(5, 122, 58);}\n"
"")
        self.pushButton_RELATORIO_2.setObjectName("pushButton_RELATORIO_2")
        self.pushButton_RELATORIO_3 = QtWidgets.QPushButton(self.frameVerdeClaro)
        self.pushButton_RELATORIO_3.setGeometry(QtCore.QRect(1610, 860, 241, 101))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_RELATORIO_3.setFont(font)
        self.pushButton_RELATORIO_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_RELATORIO_3.setStyleSheet("QPushButton{background-color:rgb(5, 122, 58);\n"
"color: rgb(243, 239, 238);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"} \n"
"QPushButton:hover{background-color:white ;color:rgb(5, 122, 58); border-color: rgb(5, 122, 58);}\n"
"")
        self.pushButton_RELATORIO_3.setObjectName("pushButton_RELATORIO_3")
        self.label = QtWidgets.QLabel(self.frameVerdeClaro)
        self.label.setGeometry(QtCore.QRect(260, 130, 1281, 41))
        self.label.setStyleSheet("background-image: url(:/newPrefix/linha.png);\n"
"background-repeat: no repeat;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/linha.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frameVerdeClaro)
        self.label_2.setGeometry(QtCore.QRect(410, 70, 971, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(0, 85, 0)")
        self.label_2.setObjectName("label_2")
        self.frame_verdeEscuro.raise_()
        self.widget_bagulhoBranco.raise_()
        self.icon_ideau.raise_()
        self.pushButton_NOVO.raise_()
        self.pushButton_EXCLUIR.raise_()
        self.pushButton_FILTRO.raise_()
        self.pushButton_RELATORIO.raise_()
        self.pushButton_RELATORIO_2.raise_()
        self.pushButton_RELATORIO_3.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.horizontalLayout.addWidget(self.frameVerdeClaro)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Controle de Patrimonio"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Código"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "Grupo"))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "Nome  do Item          "))
        self.treeWidget.headerItem().setText(3, _translate("MainWindow", "Descrição "))
        self.treeWidget.headerItem().setText(4, _translate("MainWindow", "Localização"))
        self.treeWidget.headerItem().setText(5, _translate("MainWindow", "Nº de serie"))
        self.pushButton.setText(_translate("MainWindow", "Pesquisar"))
        self.lineEdit_nome.setPlaceholderText(_translate("MainWindow", "Barra de Pesquisa"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Codigo"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Grupo"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Nome do item"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Descrição"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Localização"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Nº de Serie"))
        self.pushButton_NOVO.setText(_translate("MainWindow", "Novo"))
        self.pushButton_EXCLUIR.setText(_translate("MainWindow", "Excluir"))
        self.pushButton_FILTRO.setText(_translate("MainWindow", "Filtro"))
        self.pushButton_RELATORIO.setText(_translate("MainWindow", "Relátorio"))
        self.pushButton_RELATORIO_2.setText(_translate("MainWindow", "Cessão"))
        self.pushButton_RELATORIO_3.setText(_translate("MainWindow", "visualizar Dados"))
        self.label_2.setText(_translate("MainWindow", "Controle de Patrimônio  - Área de Cadastro"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
