import tkinter as tk
from tkinter import ttk
from database import Database

class Semestres(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        # estabelecendo a conexao com o banco de dados
        self.conexao = Database()

        # coloquem um titulo: gerenciamento de semestres
        self.title('Gerenciamento de semestres')

        # nao deixem maximizar a janela
        self.resizable(False, False)

        # definição do estilo da janela
        self.estilo = ttk.Style(self)
        self.estilo.theme_use('clam')

        # adiciona os componentes
        self.cria_widgets()

    def cria_widgets(self):
        # criar um frame de nome input_frame
        self.input_frame = ttk.Frame(self, padding=(20, 10, 20, 0))
        self.input_frame.grid(row=0, column=0)

        # criando um Label
        self.label_ano = ttk.Label(self.input_frame, text='Ano: ')
        self.label_ano.grid(row=0, column=0, sticky="W")

        # entry para ano
        self.entry_ano = ttk.Entry(self.input_frame, width=15, state='disabled')
        self.entry_ano.grid(row=0, column=1, sticky="W")
