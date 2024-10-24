# Arquivo para conexão e funções que interagem com o banco de dados
import mysql.connector # type: ignore


config = {
        'host': 'localhost',
        'database': 'cadastro', 
        'user': 'root',
        'password': ''
        }

'''config = {
        'user': 'root',
        'password': '',
        'host': 'localhost',
        'database': 'cadastro',  
        }#como estava antes'''
        
config_acess = {
        'host': 'localhost',
        'database': 'cadastro',
        'user': 'root',
        'password': ''
        }
 
'''config_acess = {
        'user': 'root',
        'password': '',
        'host': 'localhost',
        'database': 'cadastro'
        }#como estava antes'''



class bank_acess():
    def __init__(self):
        super().__init__()
        self.user = self.user
        self.cargo = self.cargo
        self.type = self.type
    def login(self):
        pass

    def register(self):
        self.user = self.user_edit_line.text()
        self.name = self.name_edit_line.text()
        self.passw = self.pass_edit_line.text()
        self.email = self.email_edit_line.text()
        self.cargo = ''
        
        


        pass

    def menu(self):
        pass

    def exit(self):
        pass

    def clear(self):
        pass

    def search(self):
        pass

    def edit(self):
        pass

    def delete(self):
        pass

    def info(self):
        pass

    def home(self):
        pass

'''INSERT INTO pessoas (nome, email, senha) VALUES ('João Pedro', 'joao.pedro@example.com', 'senha123');
''''''
cursor.execute("INSERT INTO pessoas (nome, idade, sexo, peso, altura, nacionalidade) VALUES ('João Pedro', 25, 'M', 80.5, 1.75, 'Brasileiro')")
cursor.execute("INSERT INTO pessoas (nome, idade, sexo, peso, altura, nacionalidade) VALUES ('Gabriela', 25, 'F', 80.5, 1.75, 'Brasileiro')") 
# Executa uma consulta
'''
