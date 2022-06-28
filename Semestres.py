import tkinter as tk
from tkinter import ttk
from database import Database
import re
from tkinter import messagebox

class Semestres(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        # estabelecendo a conexao com o banco de dados
        self.conexao = Database()
        self.conexao.create_tables()

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

        # carrega o treeview
        self.view_semestres()

        # criar um evento para capturar a linha selecionada
        self.treeview_semestres.bind("<<TreeviewSelect>>", self.item_selecionado_treeview)

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

        # ajustando colunas
        self.treeview_semestres.column('Ano', anchor=tk.CENTER, width=220)
        self.treeview_semestres.column('Semestre', anchor=tk.CENTER, width=220)

        self.treeview_semestres.grid(row=0, column=0, sticky='EW', pady=15)

        # adicionando uma barra de rolagem
        self.scrollbar = ttk.Scrollbar(self.treeview_frame, orient = tk.VERTICAL, command=self.treeview_semestres.yview)
        self.treeview_semestres.configure(yscroll=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=1, sticky='ns')

        # adicionando botoes
        self.botoes_frame = ttk.Frame(self)
        self.botoes_frame.grid(row=2, column=0, pady=3)

        self.botao_novo = ttk.Button(self.botoes_frame, text="Novo", command=self.novo)
        self.botao_novo.grid(row=0, column=0)
        self.botao_novo.focus()

        self.botao_salvar = ttk.Button(self.botoes_frame, state=tk.DISABLED, text="Salvar", command=self.cadastra_semestre)
        self.botao_salvar.grid(row=0, column=1)

        self.botao_alterar = ttk.Button(self.botoes_frame, state=tk.DISABLED, text="Alterar", command=self.altera_semestre)
        self.botao_alterar.grid(row=0, column=2)

        self.botao_excluir = ttk.Button(self.botoes_frame, state=tk.DISABLED, text="Excluir",
                                        command=self.excluir_semestre)
        self.botao_excluir.grid(row=0, column=3)

        self.botao_sair = ttk.Button(self.botoes_frame, text="Sair", command=self.destroy)
        self.botao_sair.grid(row=0, column=4)

    # implementar os metodos
    def novo(self):
        # deixar o botao salvar normal
        self.botao_salvar['state'] = 'NORMAL'
        # deixar o entry_ano normal
        self.entry_ano['state'] = 'NORMAL'
        # apagando o conteudo do componente entry_ano
        self.entry_ano.delete(0, tk.END)
        # mandando o foco para ele
        self.entry_ano.focus()

    def limpa_campos(self):
        self.entry_ano.delete(0, tk.END)
        self.combobox_semestre.delete(0, tk.END)

    def cadastra_semestre(self):
        # o modulo re ajuda a digitar os anos apenas no formato: 2022
        if re.findall('^2[0-9]{3}$', self.entry_ano.get()):
            linhas, erro = self.conexao.insere_semestre(self.entry_ano.get(), self.combobox_semestre.get())
            if linhas is not None:
                messagebox.showinfo(title="Sucesso", message="Semestre cadastrado com sucesso!")
                self.limpa_campos()
            else:
                if erro == 1:
                    messagebox.showwarning(title="Que pena", message="Semestre não foi cadastrado! \n "
                                                                     "Chave primária duplicada")
                else:
                    messagebox.showwarning(title="Que pena", message="Erro ao tentar cadastrar o semestre!")
        else:
            messagebox.showerror(title="Eita", message="Ano deve ser inserido com 4 digitos.Ex. 2022")

        self.limpa_campos()
        self.entry_ano.focus()
        self.view_semestres()

    def view_semestres(self):
        # limpar o treeview
        for item in self.treeview_semestres.get_children():
            self.treeview_semestres.delete(item)

        linhas = self.conexao.consulta_semestres()
        print(linhas)

        if len(linhas) > 0:
            for linha in linhas:
                self.treeview_semestres.insert("", tk.END, values=(linha[0], linha[1]))
        else:
            messagebox.showinfo(title="Aviso", message="Não existem semestres cadastrados!")


    def item_selecionado_treeview(self, event):
        self.botao_excluir['state'] = tk.NORMAL
        self.botao_alterar['state'] = tk.NORMAL
        self.entry_ano['state'] = tk.NORMAL
        self.entry_ano.delete(0, tk.END)
        self.combobox_semestre.delete(0, tk.END)

        for linha in self.treeview_semestres.selection():
            ano, semestre = self.treeview_semestres.item(linha, 'values')
            self.entry_ano.insert(tk.END, ano)
            self.combobox_semestre.set(semestre)

    def excluir_semestre(self):
        selecionado = self.treeview_semestres.focus()
        ano = self.treeview_semestres.item(selecionado, 'value')[0]
        semestre = self.treeview_semestres.item(selecionado, 'value')[1]

        resposta = messagebox.askokcancel('Confirmação', 'Deseja realmente exlcuir este semestre?')

        if resposta:
            linhas = self.conexao.deleta_semestre(ano, semestre)

            if linhas is not None:
                messagebox.showinfo(title="Sucesso", message="Semestre excluido com sucesso!")
            else:
                messagebox.showwarning(title="Que pena!", message="Não foi possível excluir o semestre")
        self.limpa_campos()
        self.botao_excluir['state'] = tk.DISABLED
        self.botao_alterar['state'] = tk.DISABLED
        self.view_semestres()

    def altera_semestre(self):
        selecionado = self.treeview_semestres.focus()
        ano = self.treeview_semestres.item(selecionado, 'value')[0]
        semestre = self.treeview_semestres.item(selecionado, 'value')[1]

        resposta = messagebox.askokcancel('Confirmação', 'Deseja realmente alterar o semestre?')

        if resposta:
            linhas = self.conexao.update_semestre(self.entry_ano.get(), self.combobox_semestre.get(), ano, semestre)

            if linhas is not None:
                messagebox.showinfo(title="Sucesso", message="Semestre alterado com sucesso!")
            else:
                messagebox.showwarning(title="Que pena!", message="Erro ao alterar o semestre!")

        self.limpa_campos()
        self.botao_alterar['state'] = tk.DISABLED
        self.botao_excluir['state'] = tk.DISABLED
        self.view_semestres()









