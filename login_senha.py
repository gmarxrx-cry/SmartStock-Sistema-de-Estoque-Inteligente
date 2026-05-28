import customtkinter as ctk
print("IMPORTANDO")
import cadastro
print("IMPORTOU")
import databaseUsuarios
#modo escuro

ctk.set_appearance_mode('dark')

app=ctk.CTk()
frameLogin = ctk.CTkFrame(app)
frameLogin.pack(fill="both", expand=True)

databaseUsuarios.criarBancoUser()

app.title("Sistema de Login")
app.geometry('300x300')


def voltarLogin():
    framecadastro.pack_forget()
    frameLogin.pack(fill="both", expand=True)

framecadastro = cadastro.criarCadastro(app, voltarLogin)
framecadastro.pack_forget()

def abrirCadastro():
    frameLogin.pack_forget()
    framecadastro.pack(fill="both", expand=True)


def conectarDados():
    print("banco conectado")


def entrar ():

    if Usuario.get() == "" or senha.get() == "":
        msg.configure(text="Por favor Preencha Os Campos")
    elif databaseUsuarios.buscaLogin(Usuario.get(), senha.get()):
        msg.configure(text="Login Realizaado")


ctk.CTkLabel(frameLogin, text="Usuario").pack()
Usuario = ctk.CTkEntry(frameLogin)
Usuario.pack()


ctk.CTkLabel(frameLogin, text="Senha").pack(pady=10)
senha = ctk.CTkEntry(frameLogin, show="*")
senha.pack()



msg = ctk.CTkLabel(frameLogin, text="")
msg.pack()


botao = ctk.CTkButton(frameLogin, text="Entrar",command=entrar)
botao.pack(pady=20)

botaoCDT = ctk.CTkButton(frameLogin, text="Novo Usuario",command=abrirCadastro)
botaoCDT.pack()


# inicia app
app.mainloop()