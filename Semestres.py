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
        self.configure(bg="#F2F2F2")

        # adiciona os componentes
        self.cria_widgets()

    def cria_widgets(self):
        # definir estilo para os widgets
        self.estilo.configure('TFrame', background='#F2F2F2')
        self.estilo.configure('TLabel', background='#F2F2F2')

        # criar um frame de nome input_frame
        self.input_frame = ttk.Frame(self, padding=(20, 10, 20, 0), style='TFrame')
        self.input_frame.grid(row=0, column=0)

        # criando um Label
        self.label_ano = ttk.Label(self.input_frame, text='Ano: ', style='TLabel')
        self.label_ano.configure(font=('Arial', 12))
        self.label_ano.grid(row=0, column=0, sticky="W")

        # entry para ano
        self.entry_ano = ttk.Entry(self.input_frame, width=15, state='disabled')
        self.entry_ano.grid(row=0, column=1, sticky="W")

        # criando um Label
        self.label_semestre = ttk.Label(self.input_frame, text='Semestre: ')
        self.label_semestre.grid(row=0, column=2, sticky="W")

        # inserindo um combobox para o semestre
        self.valor_combobox = tk.StringVar()
        self.combobox_semestre = ttk.Combobox(self.input_frame, width=14, state='readonly',
                                              textvariable=self.valor_combobox)
        self.combobox_semestre.grid(row=0, column=3, sticky="E")
        # definindo os valores do combobox
        self.combobox_semestre['values'] = ('1', '2')
        self.combobox_semestre.set(1)

        #---------------------------------------------------------------
        self.treeview_frame = ttk.Frame(self)
        self.treeview_frame.grid(row=1, column=0)

        self.colunas = ('Ano', 'Semestre')
        self.treeview_semestres = ttk.Treeview(self.treeview_frame,
                                               columns=self.colunas,
                                               show="headings", height=5)
        # definir os cabeçalhos
        self.treeview_semestres.heading('Ano', text='Ano')
        self.treeview_semestres.heading('Semestre', text='Semestre')
        self.treeview_semestres.grid(row=0, column=0, sticky='EW', pady=15)


