# Arquivo para conexão e funções que interagem com o banco de dados
import mysql.connector # type: ignore
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel
from datetime import datetime
import os, json
data_id = ''
data_user = ''
data_pass = ''
data_cargo = 15

if os.path.exists('line/dados.json'):
    print("Arquivo JSON existe.")
    v_j = json.load(open("line/dados.json"))
    data_id = v_j["idusuario"]
    data_user = v_j["user"]
    data_pass = v_j["password"]
    data_cargo = v_j["cargo"]
    print('Usuário:', data_user, 'Senha:', data_pass, 'Cargo:', data_cargo,'connect', 'ID teste:', data_id)
else:
    print("Arquivo JSON inexistente connect.")

config = {
        'host': 'localhost',
        'database': 'asset_ctrl', 
        'user': 'root',
        'password': ''
        }

        
config_acess = {
        'host': 'localhost',
        'database': 'asset_ctrl',
        'user': 'root',
        'password': ''
        }
 



def criar_conexao():
    return mysql.connector.connect(**config)

def fechar_conexao(con):
    con.close()

def conecta_view_tela(view):
    con = criar_conexao()
    cursor = con.cursor()
    cursor.execute(view)
    dados = cursor.fetchall()
    colunas = [desc[0] for desc in cursor.description]

    modelo = QStandardItemModel(len(dados), len(colunas))
    modelo.setHorizontalHeaderLabels(colunas)
    
    for idx_linha, dados_linha in enumerate(dados):
        for idx_coluna, dados_celula in enumerate(dados_linha):
            dado = QStandardItem(str(dados_celula))
            modelo.setItem(idx_linha, idx_coluna, dado) 

    cursor.close()
    fechar_conexao(con)
        
    return modelo

def conecta_procedure_tela(procedure, parametro):
    con = criar_conexao()
    cursor = con.cursor()
    cursor.callproc(procedure, [parametro])
    
    dados = []
    colunas = []
    
    resultados = cursor.stored_results()
    for resultado in resultados:
        if not colunas:
            colunas = [desc[0] for desc in resultado.description]
        dados.extend(resultado.fetchall())
    
    modelo = QStandardItemModel(len(dados), len(colunas))
    print(colunas)
    modelo.setHorizontalHeaderLabels(colunas)
    
    for idx_linha, dados_linha in enumerate(dados):
        for idx_coluna, dados_celula in enumerate(dados_linha):
            dado = QStandardItem(str(dados_celula))
            modelo.setItem(idx_linha, idx_coluna, dado) 

    cursor.close()
    fechar_conexao(con)
        
    return modelo

def update_editar_ptr(nome_ptr, valor_unitario, num_serie, num_patrimonio, data_recebimento, local, situacao, setor, categoria, idptr):
            conn = criar_conexao()
            cursor = conn.cursor()
            
            cursor.execute('select idlocal from locais where nome = %s', (local,))
            resultado_local = cursor.fetchone()
            local_sel_id = resultado_local[0]
            
            cursor.execute('select idsituacao from situacoes where nome = %s', (situacao,))
            resultado_sit = cursor.fetchone()
            sit_sel_id = resultado_sit[0]
            
            cursor.execute('select idsetor from setores_responsaveis where nome = %s', (setor,))
            resultado_set = cursor.fetchone()
            set_sel_id = resultado_set[0]
            
            cursor.execute('select idcategoria from categorias where nome = %s', (categoria,))
            resultado_cat = cursor.fetchone()
            cat_sel_id = resultado_cat[0]

            cursor.execute('''
                update patrimonios
                set
                    nome = %s,
                    valor_unitario = %s,
                    num_serie = %s,
                    num_patrimonio = %s,
                    data_recebimento = %s,
                    idlocal = %s,
                    idsituacao = %s,
                    idsetor = %s,
                    idcategoria = %s
                where idpatrimonio = %s
            ''',
                    (nome_ptr,
                    valor_unitario,
                    num_serie,
                    num_patrimonio,
                    data_recebimento,
                    local_sel_id,
                    sit_sel_id,
                    set_sel_id,
                    cat_sel_id,
                    idptr)
            )
            conn.commit()
            cursor.close()
            fechar_conexao(conn)

def infos_popular_combobox(self, id_item):
            try:
                conn = criar_conexao()
                cursor = conn.cursor()
                
                cursor.execute('select nome from categorias order by nome')
                resultado = cursor.fetchall()
                for dados in resultado:
                    self.c_item.addItem(dados[0])
                    
                cursor.execute('select nome from setores_responsaveis order by nome')
                resultado_set_resp = cursor.fetchall()
                for dados in resultado_set_resp:
                    self.c_set.addItem(dados[0])
                    
                cursor.execute('select nome from situacoes order by nome')
                resultado_situacoes = cursor.fetchall()
                for dados in resultado_situacoes:
                    self.c_sit.addItem(dados[0])
                    
                cursor.execute('select nome from locais order by nome')
                resultado_locais = cursor.fetchall()
                for dados in resultado_locais:
                    self.local_i.addItem(dados[0])
                
                cursor.callproc('st_select_editar', [id_item])

                for result in cursor.stored_results():
                    resultados = result.fetchall()
                    for resultado in resultados:
                        print(resultado)
            except Exception as e:
                print('erro', e)
            finally:
                cursor.close()
                fechar_conexao(conn)
           
            return resultado 

def deletar_ptr(id_item):
            try:
                conn = criar_conexao()
                cursor = conn.cursor()
                cursor.execute('delete from patrimonios where idpatrimonio = %s', (id_item,))
            except Exception as e:
                print('Erro ao excluir:', e)
            finally:
                conn.commit()
                cursor.close()
                fechar_conexao(conn)

# função para registrar (onde ocorreu, tipo de alteração, descrição de alteração, quem fez)
'''def registrar_log(setor, tipo_modificacao, descricao, id_usuario):
    try:
        con = config_acess
        cursor = con.cursor()

        agora = datetime.now()
        data_modificacao = agora.date()
        hora_modificacao = agora.time()

        query = 3apóstrofos
        INSERT INTO patrimonios_audit (setor, tipo_modificacao, hora_modificacao, data_modificacao, descricao, id_usuario)
        VALUES (%s, %s, %s, %s, %s, %s)
        3apóstrofos
        valores = (setor, tipo_modificacao, hora_modificacao, data_modificacao, descricao, id_usuario)

        cursor.execute(query, valores)
        con.commit()

        print("Log registrado com sucesso.")
    except Exception as e:
        print(f"Erro ao registrar o log: {e}")
    finally:
        cursor.close()
        con.close()'''

