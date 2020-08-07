from tkinter import *
from clientes_db import *
import tkMessageBox

class Application:

    root = None

    def __init__(self):

        # Cria o form e seta o titulo
        self.root = Tk()
        self.root.title("Cadastro de Cliente em Python")

        # Cria o label e a caixa de texto para o Nome
        lblNome = self.getLblNome()
        self.txtNome = self.getTxtNome()

        # Cria o label e caixa de texto para o email
        lblEmail = self.getLblEmail()
        self.txtEmail = self.getTxtEmail()

        # Cria o botao
        btnGravar = self.getBtnGravar()

        # Insere os controles no form
        lblNome.pack()
        self.txtNome.pack()
        lblEmail.pack()
        self.txtEmail.pack()
        btnGravar.pack()

        # Associa o btnGravar a uma rotina
        btnGravar.bind("<Button-1>",self.gravarCliente)

        # Seta as dimensoes do form
        self.root.geometry("250x120+0+0")

    """ Rotinas que retornam os controles para o form """

    def getLblNome(self):
        return Label(self.root,text="Nome")

    def getTxtNome(self):
        return Entry(self.root)

    def getLblEmail(self):
        return Label(self.root,text="Email")

    def getTxtEmail(self):
        return Entry(self.root)

    def getBtnGravar(self):
        return Button(self.root, text="Gravar")

    def getMainForm(self):
        return self.root

    """ Rotina para gravar o cadastro do cliente """
    def gravarCliente(self, event):
        Cliente(Nome = self.txtNome.get(),
                Email = self.txtEmail.get())
        tkMessageBox.showwarning("Cadastro de Clientes",
                                 "Cadastro gravado com sucesso!")
        sys.exit(0)

app = Application()
app.getMainForm().mainloop()