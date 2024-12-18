# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\IP\Documents\GitHub\controle_patrimonio\PATP\bckp\asset_ctrl\templates\interfaces\patr_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(880, 686)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser.setStyleSheet("background-color:transparent;")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 72))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 72))
        self.frame_2.setStyleSheet("border-radius:\n"
"10px;\n"
"border:5px solid #057A3A;\n"
"background-color: #057A3A;\n"
"border-bottom: 2px solid rgb(108, 108, 108);\n"
"border:none;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setStyleSheet("border:none;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.item_btn = QtWidgets.QPushButton(self.frame_4)
        self.item_btn.setMinimumSize(QtCore.QSize(90, 36))
        self.item_btn.setMaximumSize(QtCore.QSize(90, 36))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.item_btn.setFont(font)
        self.item_btn.setStyleSheet("QPushButton { color:rgb(254, 253, 247);\n"
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
        self.item_btn.setObjectName("item_btn")
        self.horizontalLayout_5.addWidget(self.item_btn)
        self.rlt_btn = QtWidgets.QPushButton(self.frame_4)
        self.rlt_btn.setMinimumSize(QtCore.QSize(90, 36))
        self.rlt_btn.setMaximumSize(QtCore.QSize(90, 36))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.rlt_btn.setFont(font)
        self.rlt_btn.setStyleSheet("QPushButton { color:rgb(254, 253, 247);\n"
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
        self.rlt_btn.setObjectName("rlt_btn")
        self.horizontalLayout_5.addWidget(self.rlt_btn)
        self.horizontalLayout_2.addWidget(self.frame_4, 0, QtCore.Qt.AlignLeft)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setMinimumSize(QtCore.QSize(300, 63))
        self.frame_3.setMaximumSize(QtCore.QSize(300, 63))
        self.frame_3.setStyleSheet("border:none;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:white;")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.frame_8 = QtWidgets.QFrame(self.frame_3)
        self.frame_8.setStyleSheet("border:none;")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.dt_inicial = QtWidgets.QDateEdit(self.frame_8)
        self.dt_inicial.setMinimumSize(QtCore.QSize(90, 21))
        self.dt_inicial.setMaximumSize(QtCore.QSize(120, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.dt_inicial.setFont(font)
        self.dt_inicial.setStyleSheet("QDateEdit{\n"
"color:rgb(0, 85, 0);\n"
"background-color:white;    \n"
"border-radius: 5px;\n"
"border: 1px solid #057A3A;\n"
"border-bottom: 3px solid #057A3A;\n"
"}\n"
"\n"
"\n"
"/* Estilo dos botões de navegação */\n"
"QCalendarWidget QToolButton {\n"
"    color: #FFFFFF; /* Cor do texto dos botões */\n"
"    background-color: rgb(0, 85, 0); /* Cor de fundo dos botões */\n"
"    border: none; /* Sem borda */\n"
"}")
        self.dt_inicial.setAlignment(QtCore.Qt.AlignCenter)
        self.dt_inicial.setCalendarPopup(True)
        self.dt_inicial.setObjectName("dt_inicial")
        self.horizontalLayout_3.addWidget(self.dt_inicial)
        self.dt_final = QtWidgets.QDateEdit(self.frame_8)
        self.dt_final.setMinimumSize(QtCore.QSize(90, 21))
        self.dt_final.setMaximumSize(QtCore.QSize(120, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.dt_final.setFont(font)
        self.dt_final.setStyleSheet("QDateEdit{\n"
"color:rgb(0, 85, 0);\n"
"background-color:white;    \n"
"border-radius: 5px;\n"
"border: 1px solid #057A3A;\n"
"border-bottom: 3px solid #057A3A;\n"
"\n"
"}\n"
"\n"
"\n"
"/* Estilo dos botões de navegação */\n"
"QCalendarWidget QToolButton {\n"
"    color: #FFFFFF; /* Cor do texto dos botões */\n"
"    background-color: rgb(0, 85, 0); /* Cor de fundo dos botões */\n"
"    border: none; /* Sem borda */\n"
"}")
        self.dt_final.setAlignment(QtCore.Qt.AlignCenter)
        self.dt_final.setCalendarPopup(True)
        self.dt_final.setObjectName("dt_final")
        self.horizontalLayout_3.addWidget(self.dt_final)
        self.verticalLayout_3.addWidget(self.frame_8, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_2.addWidget(self.frame_3, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.frame_9 = QtWidgets.QFrame(self.frame_2)
        self.frame_9.setMaximumSize(QtCore.QSize(120, 54))
        self.frame_9.setStyleSheet("border:none;")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.filter_dt = QtWidgets.QPushButton(self.frame_9)
        self.filter_dt.setMinimumSize(QtCore.QSize(90, 36))
        self.filter_dt.setMaximumSize(QtCore.QSize(90, 24))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.filter_dt.setFont(font)
        self.filter_dt.setStyleSheet("QPushButton { color:rgb(254, 253, 247);\n"
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
        self.filter_dt.setObjectName("filter_dt")
        self.horizontalLayout_4.addWidget(self.filter_dt)
        self.horizontalLayout_2.addWidget(self.frame_9)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_5 = QtWidgets.QFrame(self.frame_6)
        self.frame_5.setStyleSheet("border-radius:9px;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.list_patr = QtWidgets.QTableView(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.list_patr.setFont(font)
        self.list_patr.setStyleSheet("background-color:white;    \n"
"text-align:center;")
        self.list_patr.setObjectName("list_patr")
        self.verticalLayout_5.addWidget(self.list_patr)
        self.horizontalLayout.addWidget(self.frame_5)
        self.frame_7 = QtWidgets.QFrame(self.frame_6)
        self.frame_7.setStyleSheet("border-radius:9px;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:#057A3A;")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.vl_ctg = QtWidgets.QTableView(self.frame_7)
        self.vl_ctg.setStyleSheet("background-color:white;    \n"
"\n"
"")
        self.vl_ctg.setObjectName("vl_ctg")
        self.verticalLayout_4.addWidget(self.vl_ctg)
        self.label_3 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:#057A3A;")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.vl_setor = QtWidgets.QTableView(self.frame_7)
        self.vl_setor.setStyleSheet("background-color:white;    \n"
"\n"
"\n"
"")
        self.vl_setor.setObjectName("vl_setor")
        self.verticalLayout_4.addWidget(self.vl_setor)
        self.horizontalLayout.addWidget(self.frame_7)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.vl_total = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.vl_total.setFont(font)
        self.vl_total.setObjectName("vl_total")
        self.verticalLayout_2.addWidget(self.vl_total)
        self.vl_ptr = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.vl_ptr.setFont(font)
        self.vl_ptr.setObjectName("vl_ptr")
        self.verticalLayout_2.addWidget(self.vl_ptr)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600; color:#004c00;\">Esta interface foi projetada para facilitar a gestão de dados patrimoniais, permitindo o acompanhamento de informações detalhadas por categoria, setor e patrimônio individual. A funcionalidade inclui:</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-size:9pt; font-weight:600; color:#004c00;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Filtragem por Data: Selecione intervalos de datas para visualizar e analisar os dados correspondentes.</li>\n"
"<li style=\" font-size:9pt; font-weight:600; color:#004c00;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Visualização de Dados: Tabelas dinâmicas apresentam os patrimônios registrados, valores agrupados por categoria e setor.</li>\n"
"<li style=\" font-size:9pt; font-weight:600; color:#004c00;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Geração de Relatórios: Exporte os dados para arquivos Excel, garantindo praticidade na geração de documentos.</li></ul>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600; color:#004c00;\">Explore as funcionalidades para obter uma visão abrangente e detalhada de seus patrimônios de forma organizada e eficiente.</span></p></body></html>"))
        self.item_btn.setText(_translate("Form", "Produtos"))
        self.rlt_btn.setText(_translate("Form", "Relatório"))
        self.label_6.setText(_translate("Form", "    Data Inicial                            Data final"))
        self.dt_inicial.setDisplayFormat(_translate("Form", "dd/MM/yyyy"))
        self.dt_final.setDisplayFormat(_translate("Form", "dd/MM/yyyy"))
        self.filter_dt.setText(_translate("Form", "Filtrar"))
        self.label_2.setText(_translate("Form", "Valores por categoria"))
        self.label_3.setText(_translate("Form", "Valores por setores"))
        self.vl_total.setText(_translate("Form", "TextLabel"))
        self.vl_ptr.setText(_translate("Form", "TextLabel"))
