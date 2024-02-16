from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLineEdit
from TelaPrincipal import CalendarioApp

class Cadastro(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CADASTRAR")

        label = QLabel("CADASTRO")

        button = QPushButton("Cadastrar")

        labelemail = QLabel("Email")
        textoemail = QLineEdit(self)

        labelnome = QLabel("Nome Completo")
        textonome = QLineEdit(self)

        labelsenha = QLabel("Senha")
        textosenha = QLineEdit(self)

        labelsenha2 = QLabel("Confirmar Senha")
        textosenha2 =QLineEdit(self)

        self.janelapri = None

        # Crie um widget central para a janela inicial
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Use um layout QVBoxLayout para organizar os widgets
        layout = QVBoxLayout(central_widget)

        def abrirtelapri():
            if self.janelapri is None:
                self.close()
                self.janelapri = CalendarioApp()  # Crie uma nova instância apenas se ainda não existir
            self.janelapri.show()

        button.clicked.connect(abrirtelapri)

        # Configurar a imagem de fundo da janela usando QLabel
        background_image = QLabel(central_widget)
        background_image.setPixmap(QPixmap("imagens/TI.png"))
        background_image.setGeometry(0, 0, 400, 500)
        background_image.lower()  # Garanta que a imagem de fundo esteja atrás dos outros elementos

        # Layout para o label
        label_layout = QVBoxLayout()
        label_layout.addWidget(label)
        label_layout.setAlignment(label, Qt.AlignmentFlag.AlignTop)  # Alinhe o label no topo
        label_layout.setContentsMargins(63, 20, 0, 0)  # Margens específicas para o layout do label

        texto_layout = QVBoxLayout()
        texto_layout.addWidget(labelnome)
        texto_layout.addWidget(textonome)
        texto_layout.addWidget(labelemail)
        texto_layout.addWidget(textoemail)
        texto_layout.addWidget(labelsenha)
        texto_layout.addWidget(textosenha)
        texto_layout.addWidget(labelsenha2)
        texto_layout.addWidget(textosenha2)
        texto_layout.setAlignment(Qt.AlignmentFlag.AlignBottom)
        texto_layout.setContentsMargins(30, 0, 0, 0)
        texto_layout.setSpacing(5)

        # Layout para os botões
        button_layout = QVBoxLayout()
        button_layout.addWidget(button)
        button_layout.setAlignment(Qt.AlignmentFlag.AlignBottom)  # Alinhe os botões na parte inferior
        button_layout.setContentsMargins(145, 0, 0, 30)  # Margens específicas para o layout dos botões
        button_layout.setSpacing(30)

        button.setFixedSize(100, 50)
        label.setFixedSize(290, 50)
        textoemail.setFixedSize(330, 30)
        textonome.setFixedSize(330, 30)
        labelemail.setFixedSize(100, 30)
        labelnome.setFixedSize(200, 30)
        labelsenha.setFixedSize(100,30)
        labelsenha2.setFixedSize(200, 30)
        textosenha.setFixedSize(330, 30)
        textosenha2.setFixedSize(330, 30)
        label.setAutoFillBackground(False)

        # Adicione os layouts ao layout principal
        layout.addLayout(label_layout)
        layout.addLayout(texto_layout)
        layout.addLayout(button_layout)

        # Defina o estilo do texto da label
        label.setStyleSheet(
            "font-size: 50px; text-align: center; color: white; background: rgba(255, 255, 255, 0); font-weight: bold")
        labelemail.setStyleSheet(
            "font-size: 18px; color: white; background: rgba(255, 255, 255, 0); font-weight: bold")
        labelnome.setStyleSheet(
            "font-size: 18px; color: white; background: rgba(255, 255, 255, 0); font-weight: bold")
        labelsenha.setStyleSheet(
            "font-size: 18px; color: white; background: rgba(255, 255, 255, 0); font-weight: bold")
        labelsenha2.setStyleSheet(
            "font-size: 18px; color: white; background: rgba(255, 255, 255, 0); font-weight: bold")
        self.setWindowIcon(QIcon("imagens/IC.ico"))
        self.resize(400, 500)
        self.setMaximumSize(400, 500)

    def closeEvent(self, event):
        from TelaInicial import TelaInicial
        telainicio = TelaInicial()
        telainicio.show()