from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QSizePolicy
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
import os

class TelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ProgEducar - Tela Principal")
        self.setMinimumSize(800, 500)
        self.setStyleSheet("background-color: #f8f9fa;")

        self.setup_ui()

    def setup_ui(self):
        layout_principal = QHBoxLayout(self)

        # 🔹 Barra lateral
        barra_lateral = QVBoxLayout()
        barra_lateral.setSpacing(15)
        barra_lateral.setContentsMargins(10, 10, 10, 10)

        # Lista de botões (texto, ícone)
        botoes = [
            ("Alunos", "alunos.png"),
            ("Turmas", "turmas.png"),
            ("Disciplinas", "disciplinas.png"),
            ("Relatórios", "relatorios.png")
        ]

        for texto, icone_nome in botoes:
            botao = QPushButton(texto)
            botao.setIcon(QIcon(os.path.join("recursos", icone_nome)))
            botao.setIconSize(QSize(24, 24))
            botao.setMinimumHeight(40)
            botao.setStyleSheet("""
                QPushButton {
                    background-color: #ffffff;
                    border: 1px solid #ced4da;
                    border-radius: 8px;
                    padding: 5px 15px;
                    text-align: left;
                    font-size: 14px;
                }
                QPushButton:hover {
                    background-color: #e9ecef;
                }
            """)
            botao.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            barra_lateral.addWidget(botao)

        barra_lateral.addStretch()
        layout_principal.addLayout(barra_lateral)

        # 🔹 Área principal (simples por enquanto)
        area_conteudo = QLabel("Área principal do sistema")
        area_conteudo.setStyleSheet("font-size: 20px; padding: 20px;")
        layout_principal.addWidget(area_conteudo)
