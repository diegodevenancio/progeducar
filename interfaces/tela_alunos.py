from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QListWidget, QMessageBox
from PyQt5.QtCore import Qt

class TelaAlunos(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cadastro de Alunos")
        self.setMinimumSize(500, 400)
        self.setStyleSheet("background-color: #ffffff;")

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        # 🔹 Campos de entrada
        self.nome_input = QLineEdit()
        self.nome_input.setPlaceholderText("Nome do Aluno")
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email do Aluno")

        layout.addWidget(QLabel("Nome:"))
        layout.addWidget(self.nome_input)
        layout.addWidget(QLabel("Email:"))
        layout.addWidget(self.email_input)

        # 🔹 Botão de cadastro
        btn_adicionar = QPushButton("Adicionar Aluno")
        btn_adicionar.clicked.connect(self.adicionar_aluno)
        layout.addWidget(btn_adicionar)

        # 🔹 Lista de alunos
        self.lista_alunos = QListWidget()
        layout.addWidget(QLabel("Alunos Cadastrados:"))
        layout.addWidget(self.lista_alunos)

        self.setLayout(layout)

    def adicionar_aluno(self):
        nome = self.nome_input.text()
        email = self.email_input.text()

        if not nome or not email:
            QMessageBox.warning(self, "Erro", "Preencha todos os campos.")
            return

        # Apenas adiciona na lista (por enquanto, sem salvar no banco)
        self.lista_alunos.addItem(f"{nome} - {email}")

        self.nome_input.clear()
        self.email_input.clear()
        QMessageBox.information(self, "Sucesso", "Aluno cadastrado!")
