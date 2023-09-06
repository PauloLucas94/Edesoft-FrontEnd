#importando SQLite
import sqlite3 as lite

#CRUD
#Create = Inserir/ Criar
#Read = Acessar/ Mostrar
#Update = Atualizar
#Delete = Deletar/ Apagar


#criando conexão com o db
conn = lite.connect('dados.db')

#lista=['Paulo','paulo@mail.com', 123456789, "12/10/2022", 'Normal', 'Aluno sem problemas de comportamento']

#inserir 
def inserir_info(i):
    with conn:
        cur= conn.cursor()
        query = "INSERT INTO formulario (nome, email, telefone, dia_em, estado, assunto) VALUES(?, ?, ?, ?, ?, ?)"
        cur.execute(query, i)



#acessar informações

def mostrar_info():
    lista = []
    with conn:
        cur= conn.cursor()
        query = "SELECT * FROM formulario"
        cur.execute(query)
        info = cur.fetchall()
        #print(info)
        for i in info:
            lista.append(i)
    return lista

lista=['joao', 1]

def atualizar_info(i):
#atualizar informações
    with conn:
        cur= conn.cursor()
        query = "UPDATE formulario SET nome=?, email=?, telefone=?, dia_em=?, estado=?, assunto=? WHERE id=?"
        cur.execute(query, i)

#

# lista=[4]
# #deletar informações
def deletar_info(i):
        
    with conn:
        cur= conn.cursor()
        query = "DELETE FROM formulario WHERE id=? "
        cur.execute(query, i)



