import tkinter as tk
from tkinter import ttk
from Semestres import Semestres

class App(tk.Tk):
    def __init__(self):
        super(App, self).__init__()
        self.title("App da turma de 2022")
        self.configure(bg='#FFFEE1')
        self.resizable(False,False)
        self.eval('tk::PlaceWindow . center')

        self.estilo = ttk.Style(self)
        self.estilo.theme_use('clam')

        self.cria_widgets()

    def cria_widgets(self):
        # criar um frame para adicionar os componentes
        barra_de_ferramentas = tk.Frame(self, bg='#FFFEE1', padx=20, pady=20)
        barra_de_ferramentas.grid(row=0, column=0)

        # definindo estilo do botao
        self.estilo.configure('TButton', font=('arial', 12), foreground='#3D3D3D')

        # imagens para os botoes
        icone_semestre = tk.PhotoImage(file='icones/icone-semestre.png')
        # criar um botao
        botao_cadastrar_semestres = ttk.Button(barra_de_ferramentas, text='Gerenciar semestres'
                                               ,image=icone_semestre, compound=tk.TOP, style='TButton',
                                               command=self.cadastrar_semestres)
        botao_cadastrar_semestres.image = icone_semestre
        botao_cadastrar_semestres.grid(row=0, column=0, padx=5, sticky=tk.W)

    def cadastrar_semestres(self):
        window = Semestres(self)
        window.grab_set()

app = App()
app.mainloop()





