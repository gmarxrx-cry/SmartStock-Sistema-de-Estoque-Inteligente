import customtkinter as ctk
import estoque_data_base

    
def criarTelaEstoque(app):

    frameEstoque = ctk.CTkFrame(app)

    def AbrirExclusao():
        frameEstoque.pack_forget()

        telaExcluir = ExcluirProdutos(app)
        telaExcluir.pack(fill="both", expand=True)

    def AbrirListagem():
        frameEstoque.pack_forget()

        telalistar = ListarProdutos(app)
        telalistar.pack(fill="both", expand=True)

    def abrirCadastro():
        print("Abrir cadastro")
        frameEstoque.pack_forget()

        telaCadastro = cadastrarItens(app)
        telaCadastro.pack(fill="both", expand=True)


    titulo = ctk.CTkLabel(
        frameEstoque,
        text="Sistema de Estoque",
        font=("Arial", 20)
    )

    titulo.pack(pady=20)

    botaoAdicionar = ctk.CTkButton(
        frameEstoque,
        text="Adicionar Produto", command=abrirCadastro
    )
    botaoAdicionar.pack(pady=10)

    botaoListar = ctk.CTkButton(
    frameEstoque,
    text="Listar Produtos",
    command=AbrirListagem
    )
    botaoListar.pack(pady=10)

    botaoExcluir = ctk.CTkButton(
        frameEstoque,
        text="Excluir Produto",
        command=AbrirExclusao
    )
    botaoExcluir.pack(pady=10)

    return frameEstoque


def cadastrarItens(app):
    FrameEstoque = ctk.CTkFrame(app)

    nome = ctk.CTkEntry(FrameEstoque)
    nome.pack()

    quantidade = ctk.CTkEntry(FrameEstoque)
    quantidade.pack()

    preco = ctk.CTkEntry(FrameEstoque)
    preco.pack()

    vencimento = ctk.CTkEntry(FrameEstoque)
    vencimento.pack()

    msg = ctk.CTkLabel(FrameEstoque, text="")
    msg.pack()



    def cadastrar():
        nomeDTB = nome.get()
        quantidadeDTB = quantidade.get()
        precoDTB = preco.get()
        vencimentoDTB = vencimento.get()

        estoque_data_base.AdicionarProduto(
            nomeDTB,
            quantidadeDTB,
            precoDTB,
            vencimentoDTB
            )
        
        msg.configure(text="Produto cadastrado com sucesso!")

        FrameEstoque.after(
                3000,
                lambda: msg.configure(text="")
        )

        nome.delete(0, "end")
        quantidade.delete(0, "end")
        preco.delete(0, "end")
        vencimento.delete(0, "end")
        
    botaoCadastrar = ctk.CTkButton(
    FrameEstoque,
    text="Cadastrar Itens",
    command=cadastrar
    )
    botaoCadastrar.pack()

    return FrameEstoque

def ListarProdutos(app):
    framelistar = ctk.CTkFrame(app)

    titulo = ctk.CTkLabel(
        framelistar,
        text="Lista de Produtos",
    )
    titulo.pack()

    produtos = estoque_data_base.ListarProdutos()

    for produto in produtos:
        idProduto, nome, quantidade, preco, vencimento = produto
        texto = f"ID: {idProduto} | {nome} | QTD: {quantidade} | PREÇO: {preco} | VENC: {vencimento}"
    
        ctk.CTkLabel(
            framelistar,
            text=texto,
            font=("Arial", 16)
        ).pack()

def ExcluirProdutos(app):

    frameExcluir = ctk.CTkFrame(app)

    titulo = ctk.CTkLabel(
        frameExcluir,
        text="Digite o ID do produto"
    )
    titulo.pack(pady=10)

    idEntry = ctk.CTkEntry(
        frameExcluir,
        placeholder_text=""
    )
    idEntry.pack(pady=10)

    msg = ctk.CTkLabel(frameExcluir, text="")
    msg.pack(pady=10)

    def excluir():
        idProduto = idEntry.get()

        estoque_data_base.DeletarProdutos(idProduto)

        msg.configure(text="Produto Excluido!")

        idEntry.delete(0, "end")

    botaoExcluir = ctk.CTkButton(
        frameExcluir,
        text="Excluir",
        command=excluir
    )
    botaoExcluir.pack(pady=10)

    return frameExcluir