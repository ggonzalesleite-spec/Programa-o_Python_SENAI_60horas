
import tkinter as tk

# Função para capturar os dados e imprimir no console
def enviar():
    print("----- DADOS DO CLIENTE -----")
    print(f"Nome Completo: {entry_nome.get()}")
    print(f"Data de Nascimento: {entry_idade.get()}")
    print(f"E-mail: {entry_email.get()}")
    print(f"Endereço: {entry_endereco.get()}")
    print(f"Celular: {entry_celular.get()}")
    print(f"CEP: {entry_cep.get()}")
    print(f"Cidade: {entry_cidade.get()}")
    print(f"Cursos: {entry_cursos.get()}")
    print("----------------------------\n")

# Criando a janela principal
janela = tk.Tk()
janela.title("Formulário de Cadastro do Candidato")
janela.geometry("1700x750")

# Labels e Entradas
tk.Label(janela, text="Nome Completo:").pack()
entry_nome = tk.Entry(janela, width=50)
entry_nome.pack()

tk.Label(janela, text="Data de Nascimento:").pack()
entry_idade = tk.Entry(janela, width=50)
entry_idade.pack()

tk.Label(janela, text="E-mail:").pack()
entry_email = tk.Entry(janela, width=50)
entry_email.pack()

tk.Label(janela, text="Endereço:").pack()
entry_endereco = tk.Entry(janela, width=50)
entry_endereco.pack()

tk.Label(janela, text="Celular:").pack()
entry_celular = tk.Entry(janela, width=50)
entry_celular.pack()

tk.Label(janela, text="CEP:").pack()
entry_cep = tk.Entry(janela, width=50)
entry_cep.pack()

tk.Label(janela, text="Cidade:").pack()
entry_cidade = tk.Entry(janela, width=50)
entry_cidade.pack()

tk.Label(janela, text="Cursos:").pack()
entry_cursos = tk.Entry(janela, width=50)
entry_cursos.pack()

# Botão Enviar
botao = tk.Button(janela, text="Enviar", command=enviar)
botao.pack(pady=20)

# Rodar a aplicação
janela.mainloop()