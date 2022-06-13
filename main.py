import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super(App, self).__init__()
        self.title("App da turma de 2022")
        self.cria_widgets()

    def cria_widgets(self):
        # criar um frame para adicionar os componentes
        barra_de_ferramentas = tk.Frame(self, bg='#FFFEE1', padx=20, pady=20)
        barra_de_ferramentas.grid(row=0, column=0)

        # criar um botao
        botao_cadastrar_semestres = ttk.Button(barra_de_ferramentas, text='Gerenciar semestres')
        botao_cadastrar_semestres.grid(row=0, column=0, padx=5, sticky=tk.W)


app = App()
app.mainloop()





