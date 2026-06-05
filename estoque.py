import customtkinter as ctk

def criarTelaEstoque(app):

    frameEstoque = ctk.CTkFrame(app)

    titulo = ctk.CTkLabel(
        frameEstoque,
        text="Sistema de Estoque",
        font=("Arial", 20)
    )

    titulo.pack(pady=20)

    botaoAdicionar = ctk.CTkButton(
        frameEstoque,
        text="Adicionar Produto"
    )
    botaoAdicionar.pack(pady=10)

    botaoListar = ctk.CTkButton(
    frameEstoque,
    text="Listar Produtos"
    )
    botaoListar.pack(pady=10)

    botaoExcluir = ctk.CTkButton(
        frameEstoque,
        text="Excluir Produto"
    )
    botaoExcluir.pack(pady=10)

    return frameEstoque