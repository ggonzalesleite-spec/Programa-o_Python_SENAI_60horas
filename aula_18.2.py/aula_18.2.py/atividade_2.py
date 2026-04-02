
import sqlite3

# conectar ao banco de dados (se o banco não existir, ele será criado)
conn = sqlite3.connect('exemploo.db')

#  cursor para interagir com o banco de dados
cursor = conn.cursor()

# ccriando a  tabela chamada clientes
cursor.execute('''
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    idade INTEGER
)
''')

# Inserir alguns dados na tabela
cursor.execute('''
INSERT INTO clientes (id, nome, idade) VALUES (2132132,'João', 30)
''')
cursor.execute('''
INSERT INTO clientes (nome, idade) VALUES ('Maria', 25)
''')

# Salvar as mudanças
conn.commit()

# Consultar os dados na tabelinha
cursor.execute('SELECT * FROM clientes')

# com um loop acessar os resultados
for row in cursor.fetchall():
    print(row)

# fechar a conexão
conn.close()




import sqlite3
import tkinter as tk



def salvar():
    c  =  sqlite3.connect('dados.db')
    cur =  c.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS dado(nome TEXT)')
    cur.execute('INSERT INTO dado(nome) VALUES (?)', (entrada.get(),))
    
    c.commit()
    c.close()

    entrada.delete(0,tk.END)

janela  =  tk.Tk()
janela.geometry('300x300')


entrada =  tk.Entry(janela, font=('arial', 25))
entrada.pack()


btn = tk.Button(janela, text =' clique aqui', font=('arial', 25),command=salvar)
btn. pack()


janela.mainloop()
