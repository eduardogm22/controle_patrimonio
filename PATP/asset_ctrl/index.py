import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QPushButton
from connect import config, config_acess
from PyQt5.QtCore import QResource , QTimer, Qt
from PyQt5.QtGui import QIcon, QStandardItemModel, QStandardItem, QFont
import mysql.connector # type: ignore
import os
import subprocess
import json

log_list = {}

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
        self.tentativas = 0

#faltando lógica para garantir um bloqueio de tentativas de login em determinado periodo de tempo
    def login_check(self):

        try:
            if self.tentativas < 5:
                u = self.user.text()
                p = self.password.text()
                conn = mysql.connector.connect(**config_acess)
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM usuarios WHERE usuario = %s AND senha = %s", (u, p))
                filter = cursor.fetchone()
                if filter:
                    log_list['user'] = filter[1]
                    log_list['cargo'] = filter[3]
                    log_list['password'] = filter[2]
                    #print(log_list)
                    self.close()
                    self.rodar_main(str(filter[1]))
                    self.json_login()
                else:
                    print('erro')
                    self.tentativas += 1
                    print(self.tentativas)
        except Exception as e:
            print(e)

    def cancel_event(self):
        if self.user == '' and self.password == '':
            self.close()
        else:
            self.user.clear()
            self.password.clear()

    def json_login(self):
        log = {
            "user": log_list["user"],
            "cargo": log_list["cargo"],
            "password": log_list["password"]
        }
        with open("line/dados.json", "w") as info_json:
            json.dump(log, info_json)
            
    def rodar_main(self, usuario):
        subprocess.Popen(['python', 'run.py', usuario])

app = QApplication(sys.argv)
i = login_inicial()
i.show()
sys.exit(app.exec_())   