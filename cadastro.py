import customtkinter as ctk
import databaseUsuarios

def criarCadastro(app, voltarLogin):

    framecadastro = ctk.CTkFrame(app)
    def cadastrar():
        if cSenha.get() == ccSenha.get():
            msg.configure(text="Usuario Cadastrado!")
            databaseUsuarios.cadastrarUser(cUsuario.get(),
                                            cSenha.get())
            voltarLogin()
        else:
            msg.configure(text="Por favor Digite as Senhas Iguais!")

    ctk.CTkLabel(framecadastro, text="login").pack()

    cUsuario = ctk.CTkEntry(framecadastro)
    cUsuario.pack()

    ctk.CTkLabel(framecadastro, text="Senha").pack()

    cSenha = ctk.CTkEntry(framecadastro)
    cSenha.pack()

    ctk.CTkLabel(framecadastro, text="Confirme a Senha").pack()

    ccSenha = ctk.CTkEntry(framecadastro)
    ccSenha.pack()

    msg = ctk.CTkLabel(framecadastro, text="")
    msg.pack()

    botao = ctk.CTkButton(framecadastro,
                           text="Cadastrar!",
                             command=cadastrar)
    botao.pack()

    return framecadastro
