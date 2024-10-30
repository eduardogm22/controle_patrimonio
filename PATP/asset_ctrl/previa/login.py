from PyQt5 import QtCore, QtGui, QtWidgets
from imagens import resource_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint) # tira borda
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground) # deixa a tela transparente       
        MainWindow.resize(421, 641)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color : rgb(0, 191, 99);\n"
"border-radius: 25px;\n"
"")

        shadow_effect = QtWidgets.QGraphicsDropShadowEffect(self.frame)#
        shadow_effect.setBlurRadius(30)  # Grau de desfoque
        shadow_effect.setXOffset(0)  # Deslocamento horizontal
        shadow_effect.setYOffset(0)  # Deslocamento vertical
        shadow_effect.setColor(QtGui.QColor(0, 0, 0, 120))  # Cor da sombra com opacidade
        self.frame.setGraphicsEffect(shadow_effect) #]
        
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_2.addWidget(self.frame_5)
        self.frame_7 = QtWidgets.QFrame(self.frame_2)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.frame_7)
        self.label.setMaximumSize(QtCore.QSize(200, 201))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/imagens/logo__ideau.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.horizontalLayout_2.addWidget(self.frame_7)
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_8 = QtWidgets.QFrame(self.frame_6)
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.frame_8)
        self.pushButton.setMaximumSize(QtCore.QSize(40, 30))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    qproperty-iconSize: 40px 48px; \n"
"    border: none;\n"
"    background-color: rgb(0, 85, 0);\n"
"color:rgb(232, 232, 232);\n"
"border-radius: 10px\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"border-radius:10px;\n"
"background-color:#057A3A; \n"
"color:white\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border-radius: 10px;\n"
" padding-left: 5px;\n"
" padding-top:5px;\n"
" \n"
"    background-color: rgb(0, 85, 0);\n"
" \n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.frame_6)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_2.addWidget(self.frame_9)
        self.frame_10 = QtWidgets.QFrame(self.frame_6)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_2.addWidget(self.frame_10)
        self.horizontalLayout_2.addWidget(self.frame_6)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setStyleSheet("background-color: rgb(232, 232, 232);\n"
"border-radius: 25px\n"
"\n"
"\n"
"")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.frame_11 = QtWidgets.QFrame(self.frame_4)
        self.frame_11.setMinimumSize(QtCore.QSize(0, 240))
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_8.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_14 = QtWidgets.QFrame(self.frame_11)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_21 = QtWidgets.QFrame(self.frame_14)
        self.frame_21.setMaximumSize(QtCore.QSize(60, 60))
        self.frame_21.setStyleSheet("background-color:#E1DCDB;\n"
"border-radius: 0px;\n"
"    border-top-left-radius: 17px;  \n"
"    border-bottom-left-radius: 17px;")
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_21)
        self.horizontalLayout_7.setContentsMargins(1, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_2 = QtWidgets.QLabel(self.frame_21)
        self.label_2.setMaximumSize(QtCore.QSize(47, 45))
        self.label_2.setStyleSheet("background-color:#E1DCDB;\n"
"border-radius: 0px")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/imagens/imagem sem o fundo/ico.perfil.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_7.addWidget(self.label_2)
        self.horizontalLayout_5.addWidget(self.frame_21)
        self.user_2 = QtWidgets.QLineEdit(self.frame_14)
        self.user_2.setMinimumSize(QtCore.QSize(0, 30))
        self.user_2.setMaximumSize(QtCore.QSize(260, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.user_2.setFont(font)
        self.user_2.setStyleSheet("QLineEdit{\n"
"background-color:#E1DCDB;\n"
"border-radius: 0px;\n"
"padding:15px;\n"
"border-bottom: 2px solid rgb(108, 108, 108);\n"
"\n"
"    border-top-right-radius: 15px;  \n"
"    border-bottom-right-radius: 15px;\n"
"}\n"
"\n"
"\n"
"\n"
"QLineEdit:hover{background-color:rgb(238, 234, 233);color:rgb(181, 178, 177)}")
        self.user_2.setInputMask("")
        self.user_2.setText("")
        self.user_2.setObjectName("user_2")
        self.horizontalLayout_5.addWidget(self.user_2)
        self.verticalLayout_8.addWidget(self.frame_14)
        self.frame_15 = QtWidgets.QFrame(self.frame_11)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_20 = QtWidgets.QFrame(self.frame_15)
        self.frame_20.setMaximumSize(QtCore.QSize(58, 58))
        self.frame_20.setStyleSheet("background-color:#E1DCDB;\n"
"border-radius: 0px;\n"
"    border-top-left-radius: 17px;  \n"
"    border-bottom-left-radius: 17px;")
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_20)
        self.verticalLayout_9.setContentsMargins(5, 7, 4, 7)
        self.verticalLayout_9.setSpacing(4)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_3 = QtWidgets.QLabel(self.frame_20)
        self.label_3.setMaximumSize(QtCore.QSize(40, 35))
        self.label_3.setStyleSheet("background-color:#E1DCDB;\n"
"border-radius: 0px;\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/imagens/imagem sem o fundo/email.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_9.addWidget(self.label_3)
        self.horizontalLayout_6.addWidget(self.frame_20)
        self.password_3 = QtWidgets.QLineEdit(self.frame_15)
        self.password_3.setMinimumSize(QtCore.QSize(0, 30))
        self.password_3.setMaximumSize(QtCore.QSize(260, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.password_3.setFont(font)
        self.password_3.setStyleSheet("QLineEdit{\n"
"background-color:#E1DCDB;\n"
"border-radius: 0px;\n"
"padding:15px;\n"
"border-bottom: 2px solid rgb(108, 108, 108);\n"
"\n"
"    border-top-right-radius: 15px;  \n"
"    border-bottom-right-radius: 15px;\n"
"}\n"
"\n"
"QLineEdit:hover{background-color:rgb(238, 234, 233);color:rgb(181, 178, 177)}\n"
"")
        self.password_3.setInputMask("")
        self.password_3.setText("")
        self.password_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_3.setObjectName("password_3")
        self.horizontalLayout_6.addWidget(self.password_3)
        self.verticalLayout_8.addWidget(self.frame_15)
        self.verticalLayout_14.addWidget(self.frame_11)
        self.frame_12 = QtWidgets.QFrame(self.frame_4)
        self.frame_12.setMaximumSize(QtCore.QSize(16777215, 27))
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_12)
        self.pushButton_2.setMinimumSize(QtCore.QSize(250, 0))
        self.pushButton_2.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setUnderline(True)
        font.setStrikeOut(False)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    qproperty-iconSize: 40px 48px; \n"
"    border: none;\n"
"color:rgb(65, 65, 65);\n"
"border-radius: 10px\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"border-radius:10px;\n"
"\n"
"color:rgb(0, 85, 127);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
" padding-left: 5px;\n"
" padding-top:5px;\n"
" \n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_4.addWidget(self.pushButton_2, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_14.addWidget(self.frame_12)
        self.frame_16 = QtWidgets.QFrame(self.frame_4)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_16)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.goBtn_2 = QtWidgets.QPushButton(self.frame_16)
        self.goBtn_2.setMinimumSize(QtCore.QSize(123, 33))
        self.goBtn_2.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.goBtn_2.setFont(font)
        self.goBtn_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.goBtn_2.setStyleSheet("QPushButton { color: rgb(243, 239, 238);\n"
"    border-radius:25px;        \n"
"    border: 4px solid #00BF63;\n"
"    background-color:#00BF63;\n"
"    font: 13pt \"MS Shell Dlg 2\";\n"
" }\n"
"\n"
"QPushButton:hover{background-color:rgb(255, 240, 238);color:#00BF63}\n"
"\n"
"QPushButton:pressed{\n"
" padding-left: 5px;\n"
" padding-top:5px;\n"
"\n"
"}")
        self.goBtn_2.setObjectName("goBtn_2")
        self.horizontalLayout_4.addWidget(self.goBtn_2)
        self.verticalLayout_14.addWidget(self.frame_16)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 20))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout.addWidget(self.frame_3)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton.pressed.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "X"))
        self.user_2.setPlaceholderText(_translate("MainWindow", "Usuário"))
        self.password_3.setPlaceholderText(_translate("MainWindow", "Senha"))
        self.pushButton_2.setText(_translate("MainWindow", "Não tem uma conta? Cadastre-se"))
        self.goBtn_2.setText(_translate("MainWindow", "Entrar"))
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
