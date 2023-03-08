from tkinter import *
from tkinter import ttk

class InicioSesion:
    def __init__(self,raiz):
        raiz.title("inicio de sesion")

        self.usuario = StringVar()
        self.contraseña=StringVar()

        mainFrame = ttk.Frame(raiz, padding="10 20 10 20")
        mainFrame.grid(column=0, row=0)

        usuarioEntry = ttk.Entry(mainFrame, width=25,  textvariable=self.usuario)
        usuarioEntry.grid(column=1, row=0, pady=10)

        contraseñaEntry = ttk.Entry(mainFrame, width=25,  textvariable=self.contraseña)
        contraseñaEntry.grid(column=1, row=2, pady=10)

        ttk.Label(mainFrame, text="usuario:").grid(column=0, row=0, pady=10)
        ttk.Label(mainFrame, text="contraseña:").grid(column=0, row=2, pady=10)
        ttk.Button(mainFrame, text="ingresar", command=self.registrar).grid(column=1, row=4, pady=10 , sticky=(E)) 

        raiz.bind("<Return>", self.registrar)
        usuarioEntry.focus()

    def registrar(self, *args):
        print("usuario guarado")
        self.usuario.set("")
        self.contraseña.set("")

