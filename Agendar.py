import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget, QApplication
class Agenda(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("AGENDA")

        label = QLabel("AGENDA")

        button = QPushButton("Cadastre-se")

        otobutton = QPushButton("Fazer Login")

        self.janela_cadastro = None

        self.janela_login = None

        # Crie um widget central para a janela inicial
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Use um layout QVBoxLayout para organizar os widgets
        layout = QVBoxLayout(central_widget)

        # Configurar a imagem de fundo da janela usando QLabel
        background_image = QLabel(central_widget)
        background_image.setPixmap(QPixmap("imagens/TI.png"))
        background_image.setGeometry(0, 0, 400, 500)
        background_image.lower()  # Garanta que a imagem de fundo esteja atrás dos outros elementos

        # Layout para o label
        label_layout = QVBoxLayout()
        label_layout.addWidget(label)
        label_layout.setAlignment(label, Qt.AlignmentFlag.AlignTop)  # Alinhe o label no topo
        label_layout.setContentsMargins(90, 100, 0, 0)  # Margens específicas para o layout do label

        # Layout para os botões
        buttons_layout = QVBoxLayout()
        buttons_layout.addWidget(button)
        buttons_layout.addWidget(otobutton)
        buttons_layout.setAlignment(Qt.AlignmentFlag.AlignBottom)  # Alinhe os botões na parte inferior
        buttons_layout.setContentsMargins(145, 0, 0, 100)  # Margens específicas para o layout dos botões
        buttons_layout.setSpacing(30)

        button.setFixedSize(100, 50)
        otobutton.setFixedSize(100, 50)
        label.setFixedSize(235, 50)
        label.setAutoFillBackground(False)

        # Adicione os layouts ao layout principal
        layout.addLayout(label_layout)
        layout.addLayout(buttons_layout)

        # Defina o estilo do texto da label
        label.setStyleSheet("font-size: 50px; text-align: center; color: white; background: rgba(255, 255, 255, 0); font-weight: bold")
        self.setWindowIcon(QIcon("imagens/IC.ico"))
        self.resize(400, 500)
        self.setMaximumSize(400, 500)

    def on_agenda_closed(self):
        from TelaPrincipal import 
        telainicio = abrir_agendar()
        telainicio.show()