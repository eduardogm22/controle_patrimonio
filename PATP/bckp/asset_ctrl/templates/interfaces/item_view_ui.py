# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\IP\Documents\GitHub\controle_patrimonio\PATP\bckp\asset_ctrl\templates\interfaces\item_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(921, 644)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_view2 = QtWidgets.QFrame(Form)
        self.frame_view2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_view2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_view2.setObjectName("frame_view2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_view2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout.addWidget(self.frame_view2)
        self.body_item = QtWidgets.QFrame(Form)
        self.body_item.setMinimumSize(QtCore.QSize(420, 600))
        self.body_item.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.body_item.setFrameShadow(QtWidgets.QFrame.Raised)
        self.body_item.setObjectName("body_item")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.body_item)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_3 = QtWidgets.QFrame(self.body_item)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.frame_3)
        self.frame.setStyleSheet("border-radius:15px;\n"
"background-color: #057A3A;\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_8 = QtWidgets.QFrame(self.frame)
        self.frame_8.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.pushButton = QtWidgets.QPushButton(self.frame_8)
        self.pushButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(90, 36))
        self.pushButton.setMaximumSize(QtCore.QSize(90, 36))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
        self.horizontalLayout.addWidget(self.frame_8, 0, QtCore.Qt.AlignHCenter)
        self.frame_7 = QtWidgets.QFrame(self.frame)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_2.setMinimumSize(QtCore.QSize(90, 36))
        self.pushButton_2.setMaximumSize(QtCore.QSize(90, 36))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
        self.verticalLayout_8.addWidget(self.pushButton_2)
        self.horizontalLayout.addWidget(self.frame_7, 0, QtCore.Qt.AlignLeft)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setStyleSheet("border:none;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_3.setMinimumSize(QtCore.QSize(90, 36))
        self.pushButton_3.setMaximumSize(QtCore.QSize(90, 36))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
        self.verticalLayout_4.addWidget(self.pushButton_3)
        self.horizontalLayout.addWidget(self.frame_4, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.frame_3)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setMinimumSize(QtCore.QSize(450, 0))
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tb_item = QtWidgets.QTableView(self.frame_5)
        self.tb_item.setStyleSheet("background-color:white;    \n"
"border:3px solid #057A3A;\n"
"border-radius:10px\n"
"\n"
"")
        self.tb_item.setObjectName("tb_item")
        self.verticalLayout_5.addWidget(self.tb_item)
        self.horizontalLayout_2.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setMinimumSize(QtCore.QSize(210, 0))
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_6.setStyleSheet("")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.frame_6)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout_6.addWidget(self.textBrowser_2)
        self.label = QtWidgets.QLabel(self.frame_6)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.ct_view = QtWidgets.QTableView(self.frame_6)
        self.ct_view.setStyleSheet("background-color:white;    \n"
"border:3px solid #057A3A;\n"
"border-radius:10px\n"
"\n"
"")
        self.ct_view.setObjectName("ct_view")
        self.verticalLayout_6.addWidget(self.ct_view)
        self.horizontalLayout_2.addWidget(self.frame_6)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.verticalLayout_3.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.body_item)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Itens"))
        self.pushButton_2.setText(_translate("Form", "Patrimônio"))
        self.pushButton_3.setText(_translate("Form", "Relatório"))
        self.textBrowser_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600; color:#004c00;\">Gerenciamento de Itens:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600; color:#004c00;\">Esta tela permite realizar as principais ações para gerenciar itens de forma prática e direta.</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-size:9pt; font-weight:600; color:#004c00;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Cadastrar Itens: Clique em &quot;Registrar&quot; para adicionar novos itens ao sistema.</li>\n"
"<li style=\" font-size:9pt; font-weight:600; color:#004c00;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Buscar Itens: Use o campo de busca para localizar itens rapidamente. Digite uma palavra-chave e veja os resultados atualizados na tabela.</li>\n"
"<li style=\" font-size:9pt; font-weight:600; color:#004c00;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Editar Itens: Selecione um item na tabela e clique em &quot;Editar&quot; para modificar as informações.</li>\n"
"<li style=\" font-size:9pt; font-weight:600; color:#004c00;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Visualizar Detalhes: Clique em &quot;Detalhes&quot; após selecionar um item para ver informações.</li></ul>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600; color:#004c00;\">A tabela exibe os itens com as principais informações organizadas, sendo possível selecionar e interagir com os dados diretamente. Algumas funções podem ser restritas a cargos específicos para maior controle.</span></p></body></html>"))
        self.label.setText(_translate("Form", "TextLabel"))
import recurses_rc
