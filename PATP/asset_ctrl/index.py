import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QPushButton
from connect import config, config_acess
from PyQt5.QtCore import QResource , QTimer, Qt
from PyQt5.QtGui import QIcon, QStandardItemModel, QStandardItem, QFont
import mysql.connector # type: ignore
import os
import subprocess

class login_inicial(QMainWindow):
    def __init__(self):
        super().__init__()
        self.login = uic.loadUi("templates/interfaces/login.ui", self)
        self.user = self.findChild(QLineEdit, "user")
        self.password = self.findChild(QLineEdit, "password")        
        self.btn_login = self.findChild(QPushButton, "goBtn")
        self.btn_cancel = self.findChild(QPushButton, "cancelBtn")
        self.btn_login.clicked.connect(self.login_check)
        self.btn_cancel.clicked.connect(self.cancel_event)


    def login_check(self):
        if self.user.text() == 'Administrador' and self.password.text() == '123':
            u = self.user.text()
            print(u)
            self.close()
            self.rodar_main(u)
        else:
            print('erro')
            
    def cancel_event(self):
        if self.user == '' and self.password =='':
            self.close()
        else:
            self.user.clear()
            self.password.clear()

    def rodar_main(self, usuario):
        subprocess.Popen(['python', 'run.py', usuario])        

app = QApplication(sys.argv)
i = login_inicial()
i.show()
sys.exit(app.exec_())