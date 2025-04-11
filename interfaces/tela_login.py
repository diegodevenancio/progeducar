from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
)

# Importa a função de cadastro do banco de dados
from banco_dados.gerenciador_banco import cadastrar_usuario

from banco_dados.gerenciador_banco import verificar_login


class RegisterWindow(QWidget):  # Janela de cadastro de usuário
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cadastro de Usuário")
        self.setFixedSize(300, 250)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.nome_input = QLineEdit()
        self.nome_input.setPlaceholderText("Nome")
        layout.addWidget(QLabel("Nome:"))
        layout.addWidget(self.nome_input)

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")
        layout.addWidget(QLabel("Email:"))
        layout.addWidget(self.email_input)

        self.senha_input = QLineEdit()
        self.senha_input.setPlaceholderText("Senha")
        self.senha_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(QLabel("Senha:"))
        layout.addWidget(self.senha_input)

        self.btn_cadastrar = QPushButton("Cadastrar")
        self.btn_cadastrar.clicked.connect(self.cadastrar)
        layout.addWidget(self.btn_cadastrar)

        self.setLayout(layout)

    def cadastrar(self):
        nome = self.nome_input.text()
        email = self.email_input.text()
        senha = self.senha_input.text()

        if not nome or not email or not senha:
            QMessageBox.warning(self, "Erro", "Preencha todos os campos.")
            return

        sucesso = cadastrar_usuario(nome, email, senha)

        if sucesso:
            QMessageBox.information(self, "Sucesso", "Usuário cadastrado com sucesso!")
            self.close()
        else:
            QMessageBox.warning(self, "Erro", "O e-mail informado já está cadastrado.")


class LoginWindow(QWidget):  # Janela de login
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setFixedSize(300, 250)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")
        layout.addWidget(QLabel("Email:"))
        layout.addWidget(self.email_input)

        self.senha_input = QLineEdit()
        self.senha_input.setPlaceholderText("Senha")
        self.senha_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(QLabel("Senha:"))
        layout.addWidget(self.senha_input)

        self.btn_login = QPushButton("Entrar")
        self.btn_login.clicked.connect(self.login)
        layout.addWidget(self.btn_login)

        # Novo botão de cadastro
        self.btn_cadastrar = QPushButton("Cadastrar")
        self.btn_cadastrar.clicked.connect(self.abrir_cadastro)
        layout.addWidget(self.btn_cadastrar)

        self.setLayout(layout)

    def login(self):
        email = self.email_input.text()  # Pega o email digitado
        senha = self.senha_input.text()  # Pega a senha digitada

        # Verifica se os campos estão preenchidos
        if not email or not senha:
            QMessageBox.warning(self, "Erro", "Preencha todos os campos.")
            return
        
        from banco_dados.gerenciador_banco import autenticar_usuario

        # Verifica se o login está correto no banco
        if autenticar_usuario(email, senha):
            QMessageBox.information(self, "Sucesso", "Login realizado com sucesso!")
            # Aqui você pode chamar a próxima janela do sistema depois do login
        else:
            QMessageBox.warning(self, "Erro", "Email ou senha inválidos.")

    def abrir_cadastro(self):
        from interfaces.tela_login import RegisterWindow
        self.cadastro_janela = RegisterWindow()
        self.cadastro_janela.show()
