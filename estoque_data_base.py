import sqlite3

def CriarTabelaEstoque():
    db = sqlite3.connect("estoque.db")
    cursor = db.cursor()
    cursor.execute("""
CREATE TABLE IF NOT EXISTS Estoque(
    id INTEGER PRIMARY KEY,
    nomeProduto TEXT,
    quantidade INTEGER,
    preco REAL,
    vencimento TEXT               
)
""")
    
    db.commit()
    db.close()

def AdicionarProduto(nomeProduto, quantidade, preco, vencimento):
    db = sqlite3.connect("estoque.db")
    cursor = db.cursor()

    cursor.execute("""
INSERT INTO estoque (nomeProduto, quantidade, preco, vencimento)
VALUES(?, ?, ?, ?)                  
""", (nomeProduto, quantidade, preco, vencimento))
    
    db.commit()
    db.close()

def ListarProdutos():
    db = sqlite3.connect("estoque.db")
    cursor = db.cursor()

    cursor.execute("SELECT * FROM estoque")
    dados = cursor.fetchall()

    db.close()
    return dados

def DeletarProdutos(id):
    db = sqlite3.connect("estoque.db")
    cursor = db.cursor()

    cursor.execute("DELETE FROM estoque WHERE id = ?", (id,))

    db.commit()
    db.close()

CriarTabelaEstoque()

#AdicionarProduto("Arroz", 10, 5,99)