import sqlite3

def buscaLogin(usuarioLog, senhaLog):

    db = sqlite3.connect("usuarios.db")
    cursor = db.cursor()

    cursor.execute("""
                   SELECT * FROM usuarios
                   WHERE usuario = ? AND senha = ?
                   """,
                   (usuarioLog, senhaLog))
    
    resultado = cursor.fetchone()
    db.close()

    return resultado is not None     

def criarBancoUser():
    db = sqlite3.connect("usuarios.db")
    cursor = db.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT,
        senha TEXT
    )
    """)
    db.commit()
    db.close()



def cadastrarUser(usuario, senha):
    db = sqlite3.connect("usuarios.db")
    cursor = db.cursor()
    cursor.execute("""
    INSERT INTO usuarios (usuario, senha)
    VALUES (?, ?)
    """, (usuario, senha))
    db.commit()
    db.close()