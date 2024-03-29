import re
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLineEdit, QDialog, QApplication
from TelaPrincipal import CalendarioApp
import json
class Logar(QMainWindow):
    def __init__(self):
        super().__init__()
        nome_arquivo = "dados.json"

        # Ler o conteúdo do arquivo JSON
        with open(nome_arquivo, "r") as arquivo:
            dados = json.load(arquivo)

        self.setWindowTitle("LOGIN")

        label = QLabel("LOGIN")

        button = QPushButton("Fazer Login")

        labelemail = QLabel("Email")
        textoemail = QLineEdit(self)

        labelsenha = QLabel("Senha")
        textosenha = QLineEdit(self)

        labelerro = QLabel("Usuário e/ou senha incorretos.")
        labelerro.hide()

        buttonesq = QPushButton("Esqueci minha senha")

        self.contador = 0
        self.janelapri = None

        def abrir_esq():
            dialog = QDialog()
            main_layout = QVBoxLayout()
            content_layout = QVBoxLayout()
            button_layout = QVBoxLayout()
            dialog.setWindowTitle("ESQUECI MINHA SENHA")
            dialog.setWindowIcon(QIcon("imagens/IC.ico"))
            labelavi = QLabel("Funcionalidade indisponível.")
            buttonavi = QPushButton("Fechar")
            buttonavi.setFixedSize(100, 30)
            content_layout.addWidget(labelavi)
            content_layout.setContentsMargins(15, 0, 0, 0)

            button_layout.addWidget(buttonavi)
            button_layout.setAlignment(Qt.AlignmentFlag.AlignBottom)
            button_layout.setContentsMargins(40, 0, 0, 0)

            main_layout.addLayout(content_layout)
            main_layout.addLayout(button_layout)

            buttonavi.clicked.connect(dialog.close)

            dialog.setLayout(main_layout)
            dialog.resize(200, 80)
            dialog.setMaximumSize(200, 80)
            dialog.exec()







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
        label_layout.setContentsMargins(120, 0, 0, 0)  # Margens específicas para o layout do label

        texto_layout = QVBoxLayout()
        texto_layout.addWidget(labelemail)
        texto_layout.addWidget(textoemail)
        texto_layout.addWidget(labelsenha)
        texto_layout.addWidget(textosenha)
        texto_layout.setAlignment(Qt.AlignmentFlag.AlignBottom)
        texto_layout.setContentsMargins(30, 0, 0, 0)
        texto_layout.setSpacing(10)

        esqlayout = QVBoxLayout()
        esqlayout.addWidget(buttonesq)
        esqlayout.setAlignment(Qt.AlignmentFlag.AlignBottom)
        esqlayout.setContentsMargins(30, 0, 0, 40)

        errolayout = QVBoxLayout()
        errolayout.addWidget(labelerro)
        labelerro.hide()
        errolayout.setContentsMargins(30, 0, 0, 0)
        labelerro.setFixedSize(200, 20)
        labelerro.setStyleSheet("color: red; font-weight: bold; background-color: purple")

        # Layout para os botões
        button_layout = QVBoxLayout()
        button_layout.addWidget(button)
        button_layout.setAlignment(Qt.AlignmentFlag.AlignBottom)  # Alinhe os botões na parte inferior
        button_layout.setContentsMargins(145, 0, 0, 30)  # Margens específicas para o layout dos botões
        button_layout.setSpacing(30)

        button.setFixedSize(100, 50)
        label.setFixedSize(150, 50)
        textoemail.setFixedSize(330, 30)
        labelemail.setFixedSize(100, 30)
        labelsenha.setFixedSize(100,30)
        textosenha.setFixedSize(330, 30)
        buttonesq.setFixedSize(150, 40)
        label.setAutoFillBackground(False)

        # Adicione os layouts ao layout principal
        layout.addLayout(label_layout)
        layout.addLayout(texto_layout)
        layout.addLayout(esqlayout)
        layout.addLayout(errolayout)
        layout.addLayout(button_layout)

        buttonesq.clicked.connect(abrir_esq)

        # Defina o estilo do texto da label
        label.setStyleSheet(
            "font-size: 50px; text-align: center; color: white; background: rgba(255, 255, 255, 0); font-weight: bold")
        labelemail.setStyleSheet(
            "font-size: 18px; color: white; background: rgba(255, 255, 255, 0); font-weight: bold")
        labelsenha.setStyleSheet(
            "font-size: 18px; color: white; background: rgba(255, 255, 255, 0); font-weight: bold")
        self.setWindowIcon(QIcon("imagens/IC.ico"))
        self.resize(400, 500)
        self.setMaximumSize(400, 500)





        def abrirtelapri():
            if self.janelapri is None:
                self.close()
                self.janelapri = CalendarioApp(self.contador)  # Crie uma nova instância apenas se ainda não existir
            self.janelapri.show()


        def condicoes():
            labelerro.hide()

            for self.contador in range(len(dados["dadosusuario"]["email"])):
                if textoemail.text() == dados["dadosusuario"]["email"][self.contador] and textosenha.text() == \
                        dados["dadosusuario"]["senha"][self.contador]:
                    abrirtelapri()
                else:
                    labelerro.show()
                    self.contador = 0



        button.clicked.connect(condicoes)

    def closeEvent(self, event):
        from TelaInicial import TelaInicial
        telainicio = TelaInicial()
        telainicio.show()
