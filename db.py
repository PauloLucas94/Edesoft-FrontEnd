#importando SQLite
import sqlite3 as lite

#criando conexao
conn = lite.connect('dados.db')

#criando tabela
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE formulario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT, telefone TEXT, dia_em DATE, estado TEXT, assunto TEXT)")
