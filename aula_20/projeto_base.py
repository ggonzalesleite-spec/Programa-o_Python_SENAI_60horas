import sqlite3 # banco de dados 
import tkinter as tk # lib de interface grafica 
from tkinter import messagebox, ttk # caixa de msg / tkinter


def conectar():
    return sqlite3.connect('teste.db')

conectar()

# CREATE READ UPDATE DELETE

# banco de dados
def criar_tabela():
    conn = conectar()
    c = conn.cursor() # digitar sql num arquivo python 
    c.execute('''
              CREATE TABLE IF NOT EXISTS usuarios(
              
              id INTEGER NOT NULL,
              nome TEXT NOT NULL,
              email TEXT NOT NULL
              
        
              
             )''')
    conn.commit()
    conn.close()
    
# Interface grafica

janela = tk.Tk()
janela.geometry('650x500')
janela.title('...CRUD...')

style = ttk.Style()
style.theme_use('clam')
style.configure('Tlabel', background = 'black', font = ('Segoe UI', 10 ))
style.configure('TEntry',fort = ('Segoe UI', 10 ))
style.configure('Tbutton', font = ('Segoe UI', 10), padding = 6 )
style.configure('treeview.heding', font = ('Segoe UI', 10 , 'bold'))
style.configure('treeview', font = ('Segoe UI', 10 , 'bold'))



main_frame = ttk.Frame(janela, padding = 15)
main_frame.pack(fill= tk.BOTH, expand=True)

# widgets - elementos

titulo = ttk.Label(main_frame, text='sistema de cadastro', font =('Segoe UI', 10, 'bold'))
titulo.grid(row=0, columnspan=2, pady=(0,15), sticky = 'w')

    
