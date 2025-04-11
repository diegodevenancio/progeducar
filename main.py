import sys
import os
from PyQt5.QtWidgets import QApplication

# Importações dos módulos do sistema
from interfaces.tela_login import LoginWindow
from banco_dados.gerenciador_banco import init_db

# Garante que a pasta do banco exista
os.makedirs('banco_dados', exist_ok=True)

# Inicializa o banco de dados (cria o arquivo e a tabela, se não existirem)
init_db()

# Cria a aplicação PyQt
app = QApplication(sys.argv)

# Abre a janela de login
janela = LoginWindow()
janela.show()

# Executa o loop da aplicação
sys.exit(app.exec_())
