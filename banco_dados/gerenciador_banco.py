import sqlite3  # Biblioteca para manipulação de banco SQLite
import os       # Biblioteca para lidar com caminhos de arquivos

# Caminho padrão para o arquivo do banco de dados
CAMINHO_BANCO = os.path.join('banco_dados', 'progeducar.db')

def init_db():
    """
    Inicializa o banco de dados: cria o arquivo e a tabela de usuários se não existirem.
    """
    # Conecta ao banco de dados (cria o arquivo se não existir)
    conn = sqlite3.connect(CAMINHO_BANCO)
    cursor = conn.cursor()

    # Cria a tabela 'usuarios' com os campos necessários
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL
        )
    ''')

    # Salva as alterações e fecha a conexão
    conn.commit()
    conn.close()

def cadastrar_usuario(nome, email, senha):
    """
    Cadastra um novo usuário no banco de dados.
    Retorna True se o cadastro for bem-sucedido, False se o e-mail já existir.
    """
    conn = sqlite3.connect(CAMINHO_BANCO)
    cursor = conn.cursor()

    # Verifica se já existe um usuário com o mesmo e-mail
    cursor.execute("SELECT id FROM usuarios WHERE email = ?", (email,))
    if cursor.fetchone():
        conn.close()
        return False  # Usuário já existe

    # Insere os dados do novo usuário
    cursor.execute(
        "INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)",
        (nome, email, senha)
    )

    # Salva e fecha
    conn.commit()
    conn.close()
    return True

def autenticar_usuario(email, senha):
    """
    Verifica se existe um usuário com o e-mail e senha fornecidos.
    Retorna True se existir, False caso contrário.
    """
    conn = sqlite3.connect(CAMINHO_BANCO)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE email = ? AND senha = ?", (email, senha))
    usuario = cursor.fetchone()

    conn.close()

    return usuario is not None

def verificar_login(email, senha):
    """
    Verifica se o email e senha estão corretos no banco de dados.
    Retorna True se estiverem corretos, False caso contrário.
    """
    conn = sqlite3.connect(CAMINHO_BANCO)
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM usuarios WHERE email = ? AND senha = ?", (email, senha))
    usuario = cursor.fetchone()

    conn.close()

    return usuario is not None
