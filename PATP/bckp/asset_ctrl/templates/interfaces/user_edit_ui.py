# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\IP\Documents\GitHub\controle_patrimonio\PATP\bckp\asset_ctrl\templates\interfaces\user_edit.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(826, 644)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_user_details = QtWidgets.QFrame(Form)
        self.frame_user_details.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_user_details.setStyleSheet("background-color: 0;\n"
"border-bottom:0")
        self.frame_user_details.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_user_details.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_user_details.setObjectName("frame_user_details")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_user_details)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout.addWidget(self.frame_user_details)
        self.frame_info = QtWidgets.QFrame(Form)
        self.frame_info.setMinimumSize(QtCore.QSize(0, 600))
        self.frame_info.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_info.setObjectName("frame_info")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_info)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_6 = QtWidgets.QFrame(self.frame_info)
        self.frame_6.setStyleSheet("background-color:0;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame_6)
        self.frame_2.setMinimumSize(QtCore.QSize(490, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(490, 16777215))
        self.frame_2.setStyleSheet("background-color : rgba(0, 191, 99,199);\n"
"border-radius: 15px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setMinimumSize(QtCore.QSize(0, 60))
        self.label.setMaximumSize(QtCore.QSize(16777215, 90))
        self.label.setStyleSheet("background-color: 0;\n"
"border-bottom:0")
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.user_line = QtWidgets.QLineEdit(self.frame_2)
        self.user_line.setMinimumSize(QtCore.QSize(300, 27))
        self.user_line.setMaximumSize(QtCore.QSize(300, 27))
        self.user_line.setStyleSheet("QLineEdit{\n"
"    color:rgb(8, 8, 8);\n"
"background-color:white;\n"
"border-radius: 5px;\n"
"border-bottom: 1px solid rgb(91, 91, 91)\n"
"}\n"
"\n"
"QLineEdit:hover{background-color:rgb(238, 234, 233);color:rgb(181, 178, 177)}")
        self.user_line.setObjectName("user_line")
        self.verticalLayout_6.addWidget(self.user_line, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame_6)
        self.frame_3.setStyleSheet("background-color : rgba(0, 191, 99,199);\n"
"border-radius: 15px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_9 = QtWidgets.QFrame(self.frame_3)
        self.frame_9.setStyleSheet("background-color: 0;\n"
"border-bottom:0")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 33))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton { color:rgb(254, 253, 247);\n"
"    border-radius:10px;        \n"
"    border: 4px solid rgb(255, 255, 255);\n"
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
        self.verticalLayout_5.addWidget(self.pushButton_3)
        self.horizontalLayout_3.addWidget(self.frame_9, 0, QtCore.Qt.AlignBottom)
        self.frame_10 = QtWidgets.QFrame(self.frame_3)
        self.frame_10.setStyleSheet("background-color: 0;\n"
"border-bottom:0")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 33))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton { color:rgb(254, 253, 247);\n"
"    border-radius:10px;        \n"
"    border: 4px solid rgb(255, 255, 255);\n"
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
        self.verticalLayout_3.addWidget(self.pushButton_2)
        self.horizontalLayout_3.addWidget(self.frame_10, 0, QtCore.Qt.AlignTop)
        self.frame_11 = QtWidgets.QFrame(self.frame_3)
        self.frame_11.setStyleSheet("background-color: 0;\n"
"border-bottom:0")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton = QtWidgets.QPushButton(self.frame_11)
        self.pushButton.setMinimumSize(QtCore.QSize(90, 90))
        self.pushButton.setMaximumSize(QtCore.QSize(90, 90))
        self.pushButton.setStyleSheet("background-color:rgba(255, 255, 255,199);\n"
"border:3px solid #057A3A;\n"
"border-radius:10px")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_4.addWidget(self.pushButton)
        self.horizontalLayout_3.addWidget(self.frame_11, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout.addWidget(self.frame_3)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.frame_4 = QtWidgets.QFrame(self.frame_info)
        self.frame_4.setStyleSheet("background-color : rgba(0, 191, 99,199);\n"
"border-radius: 15px;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_7 = QtWidgets.QFrame(self.frame_4)
        self.frame_7.setMaximumSize(QtCore.QSize(490, 16777215))
        self.frame_7.setStyleSheet("background-color: 0;\n"
"border-bottom:0")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.pass_line_info = QtWidgets.QLineEdit(self.frame_7)
        self.pass_line_info.setMinimumSize(QtCore.QSize(0, 27))
        self.pass_line_info.setMaximumSize(QtCore.QSize(16777215, 27))
        self.pass_line_info.setStyleSheet("QLineEdit{\n"
"    color:rgb(8, 8, 8);\n"
"background-color:white;\n"
"border-radius: 5px;\n"
"border-bottom: 1px solid rgb(91, 91, 91)\n"
"}\n"
"\n"
"QLineEdit:hover{background-color:rgb(238, 234, 233);color:rgb(181, 178, 177)}")
        self.pass_line_info.setObjectName("pass_line_info")
        self.verticalLayout_7.addWidget(self.pass_line_info)
        self.name_user_info = QtWidgets.QLineEdit(self.frame_7)
        self.name_user_info.setMinimumSize(QtCore.QSize(0, 27))
        self.name_user_info.setMaximumSize(QtCore.QSize(16777215, 27))
        self.name_user_info.setStyleSheet("QLineEdit{\n"
"    color:rgb(8, 8, 8);\n"
"background-color:white;\n"
"border-radius: 5px;\n"
"border-bottom: 1px solid rgb(91, 91, 91)\n"
"}\n"
"\n"
"QLineEdit:hover{background-color:rgb(238, 234, 233);color:rgb(181, 178, 177)}")
        self.name_user_info.setObjectName("name_user_info")
        self.verticalLayout_7.addWidget(self.name_user_info)
        self.email_user_info = QtWidgets.QLineEdit(self.frame_7)
        self.email_user_info.setMinimumSize(QtCore.QSize(0, 27))
        self.email_user_info.setMaximumSize(QtCore.QSize(16777215, 27))
        self.email_user_info.setStyleSheet("QLineEdit{\n"
"    color:rgb(8, 8, 8);\n"
"background-color:white;\n"
"border-radius: 5px;\n"
"border-bottom: 1px solid rgb(91, 91, 91)\n"
"}\n"
"\n"
"QLineEdit:hover{background-color:rgb(238, 234, 233);color:rgb(181, 178, 177)}")
        self.email_user_info.setObjectName("email_user_info")
        self.verticalLayout_7.addWidget(self.email_user_info)
        self.horizontalLayout_2.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame_4)
        self.frame_8.setMinimumSize(QtCore.QSize(300, 0))
        self.frame_8.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_8.setStyleSheet("background-color: 0;\n"
"border-bottom:0")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_2 = QtWidgets.QLabel(self.frame_8)
        self.label_2.setMinimumSize(QtCore.QSize(0, 25))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_8.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.comboBox = QtWidgets.QComboBox(self.frame_8)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 27))
        self.comboBox.setMaximumSize(QtCore.QSize(16777215, 27))
        self.comboBox.setStyleSheet("QComboBox{background-color:white;\n"
"border-radius: 15px;\n"
"border-radius: 5px;\n"
"border-bottom: 1px solid rgb(91, 91, 91)}\n"
"\n"
"\n"
" ")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.verticalLayout_8.addWidget(self.comboBox)
        self.horizontalLayout_2.addWidget(self.frame_8, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_info)
        self.frame_5.setStyleSheet("background-color:0;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_12 = QtWidgets.QFrame(self.frame_5)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_14 = QtWidgets.QFrame(self.frame_12)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_14)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_3 = QtWidgets.QLabel(self.frame_14)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_9.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.frame_14)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_9.addWidget(self.label_4)
        self.horizontalLayout_5.addWidget(self.frame_14)
        self.frame_15 = QtWidgets.QFrame(self.frame_12)
        self.frame_15.setMinimumSize(QtCore.QSize(400, 0))
        self.frame_15.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_15)
        self.pushButton_5.setMinimumSize(QtCore.QSize(90, 40))
        self.pushButton_5.setMaximumSize(QtCore.QSize(90, 50))
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("QPushButton { color:rgb(254, 253, 247);\n"
"    border-radius:15px;        \n"
"    border: 4px solid rgb(255, 255, 255);\n"
"    background-color: rgb(0, 85, 0);\n"
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
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_4.addWidget(self.pushButton_5, 0, QtCore.Qt.AlignTop)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_15)
        self.pushButton_6.setMinimumSize(QtCore.QSize(90, 40))
        self.pushButton_6.setMaximumSize(QtCore.QSize(90, 50))
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet("QPushButton { color:rgb(254, 253, 247);\n"
"    border-radius:15px;        \n"
"    border: 4px solid rgb(255, 255, 255);\n"
"    background-color: rgb(0, 85, 0);\n"
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
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_4.addWidget(self.pushButton_6, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_5.addWidget(self.frame_15, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_10.addWidget(self.frame_12)
        self.frame_13 = QtWidgets.QFrame(self.frame_5)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_10.addWidget(self.frame_13, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.verticalLayout.addWidget(self.frame_info)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "user_info"))
        self.user_line.setText(_translate("Form", "Usuário"))
        self.pushButton_3.setText(_translate("Form", "btn_edit"))
        self.pushButton_2.setText(_translate("Form", "btn_foto"))
        self.pushButton.setText(_translate("Form", "FOTO"))
        self.pass_line_info.setText(_translate("Form", "Senha"))
        self.name_user_info.setText(_translate("Form", "Nome"))
        self.email_user_info.setText(_translate("Form", "Email"))
        self.label_2.setText(_translate("Form", "TextLabel"))
        self.comboBox.setItemText(0, _translate("Form", "Cargo"))
        self.label_3.setText(_translate("Form", "Data ultima alteração"))
        self.label_4.setText(_translate("Form", "Quem alterou."))
        self.pushButton_5.setText(_translate("Form", "cancel_btn"))
        self.pushButton_6.setText(_translate("Form", "confirm_btn"))
