# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\IP\Desktop\PATP\asset_ctrl\templates\interfaces\forn_config.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(914, 378)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_7 = QtWidgets.QFrame(Form)
        self.frame_7.setMinimumSize(QtCore.QSize(0, 360))
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 360))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.frame_7)
        self.frame_2.setMaximumSize(QtCore.QSize(450, 16777215))
        self.frame_2.setStyleSheet("border-radius:10px;\n"
"background-color: #057A3A;\n"
"border-bottom: 2px solid rgb(108, 108, 108);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setMaximumSize(QtCore.QSize(450, 16777215))
        self.frame_6.setStyleSheet("border:none;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_10 = QtWidgets.QFrame(self.frame_6)
        self.frame_10.setStyleSheet("border:0;\n"
"background-color:transparent;")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.box_forn = QtWidgets.QComboBox(self.frame_10)
        self.box_forn.setMinimumSize(QtCore.QSize(240, 24))
        self.box_forn.setMaximumSize(QtCore.QSize(240, 24))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.box_forn.setFont(font)
        self.box_forn.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.box_forn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.box_forn.setStyleSheet("\n"
"\n"
"\n"
"QComboBox{background-color:white;\n"
"border-radius: 50px;\n"
"\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    width: 25px; /* Largura do quadrado */\n"
"align-itens:center;\n"
"}\n"
"\n"
" ")
        self.box_forn.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.box_forn.setObjectName("box_forn")
        self.verticalLayout_7.addWidget(self.box_forn, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.horizontalLayout.addWidget(self.frame_10, 0, QtCore.Qt.AlignVCenter)
        self.frame_12 = QtWidgets.QFrame(self.frame_6)
        self.frame_12.setStyleSheet("border:0;")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_12)
        self.pushButton_7.setMinimumSize(QtCore.QSize(71, 33))
        self.pushButton_7.setMaximumSize(QtCore.QSize(70, 33))
        self.pushButton_7.setStyleSheet("QPushButton { color:rgb(254, 253, 247);\n"
"    border-radius:15px;        \n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    background-color: rgb(0, 76, 0)\n"
"\n"
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
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_6.addWidget(self.pushButton_7)
        self.horizontalLayout.addWidget(self.frame_12)
        self.verticalLayout_4.addWidget(self.frame_6, 0, QtCore.Qt.AlignHCenter)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setStyleSheet("border:none;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.frame_5)
        self.label.setStyleSheet("border:none;\n"
"color:white;")
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        self.label_2.setStyleSheet("border:none;\n"
"color:white;")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.frame_5)
        self.label_3.setStyleSheet("border:none;\n"
"color:white;")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.verticalLayout_4.addWidget(self.frame_5)
        self.horizontalLayout_3.addWidget(self.frame_2)
        self.frame_8 = QtWidgets.QFrame(self.frame_7)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_4 = QtWidgets.QFrame(self.frame_8)
        self.frame_4.setStyleSheet("")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.frame_4)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.name_line = QtWidgets.QLineEdit(self.frame_4)
        self.name_line.setMinimumSize(QtCore.QSize(0, 24))
        self.name_line.setMaximumSize(QtCore.QSize(16777215, 24))
        self.name_line.setStyleSheet("\n"
"QLineEdit{\n"
"background-color:white;    \n"
"border-radius: 5px;\n"
"border: 1px solid #057A3A;\n"
"border-bottom: 3px solid #057A3A;\n"
"\n"
"    border-top-right-radius: 5px;  \n"
"    border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"")
        self.name_line.setObjectName("name_line")
        self.verticalLayout_2.addWidget(self.name_line)
        self.label_6 = QtWidgets.QLabel(self.frame_4)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.cnpj_line = QtWidgets.QLineEdit(self.frame_4)
        self.cnpj_line.setMinimumSize(QtCore.QSize(0, 24))
        self.cnpj_line.setMaximumSize(QtCore.QSize(16777215, 24))
        self.cnpj_line.setStyleSheet("\n"
"QLineEdit{\n"
"background-color:white;    \n"
"border-radius: 5px;\n"
"border: 1px solid #057A3A;\n"
"border-bottom: 3px solid #057A3A;\n"
"\n"
"    border-top-right-radius: 5px;  \n"
"    border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"")
        self.cnpj_line.setObjectName("cnpj_line")
        self.verticalLayout_2.addWidget(self.cnpj_line)
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.horizontalLayout_4.addWidget(self.frame_4, 0, QtCore.Qt.AlignVCenter)
        self.frame_9 = QtWidgets.QFrame(self.frame_8)
        self.frame_9.setMinimumSize(QtCore.QSize(90, 90))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_8.setMinimumSize(QtCore.QSize(72, 33))
        self.pushButton_8.setMaximumSize(QtCore.QSize(72, 33))
        self.pushButton_8.setStyleSheet("QPushButton { color:rgb(254, 253, 247);\n"
"    border-radius:15px;        \n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    background-color: rgb(0, 76, 0)\n"
"\n"
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
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_9.addWidget(self.pushButton_8)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_2.setMinimumSize(QtCore.QSize(72, 33))
        self.pushButton_2.setMaximumSize(QtCore.QSize(72, 33))
        self.pushButton_2.setStyleSheet("QPushButton { color:rgb(254, 253, 247);\n"
"    border-radius:15px;        \n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    background-color: rgb(0, 76, 0)\n"
"\n"
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
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_9.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_3.setMaximumSize(QtCore.QSize(72, 33))
        self.pushButton_3.setStyleSheet("QPushButton { color:rgb(254, 253, 247);\n"
"    border-radius:15px;        \n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    background-color: rgb(0, 76, 0)\n"
"\n"
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
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_9.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(self.frame_9)
        self.pushButton.setMinimumSize(QtCore.QSize(72, 33))
        self.pushButton.setMaximumSize(QtCore.QSize(72, 33))
        self.pushButton.setStyleSheet("QPushButton { color:rgb(254, 253, 247);\n"
"    border-radius:15px;        \n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    background-color: rgb(0, 76, 0)\n"
"\n"
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
"}")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_9.addWidget(self.pushButton)
        self.horizontalLayout_4.addWidget(self.frame_9)
        self.horizontalLayout_3.addWidget(self.frame_8)
        self.verticalLayout.addWidget(self.frame_7)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_7.setText(_translate("Form", "+"))
        self.label.setText(_translate("Form", "Fornecedores cadastrados"))
        self.label_2.setText(_translate("Form", "Último fornecedor cadastrado"))
        self.label_3.setText(_translate("Form", "Última modificação:"))
        self.label_5.setText(_translate("Form", "Nome"))
        self.label_6.setText(_translate("Form", "CNPJ"))
        self.label_4.setText(_translate("Form", "Data de Criação:"))
        self.pushButton_8.setText(_translate("Form", "Editar"))
        self.pushButton_2.setText(_translate("Form", "Confirmar"))
        self.pushButton_3.setText(_translate("Form", "Cancelar"))
        self.pushButton.setText(_translate("Form", "Deletar"))
