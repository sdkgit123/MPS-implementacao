import re
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLineEdit, QDialog, QApplication
from TelaPrincipal import CalendarioApp
import json




class Cadastro(QMainWindow):
    def __init__(self):
        super().__init__()
        nome_arquivo = "dados.json"

        # Ler o conteúdo do arquivo JSON
        with open(nome_arquivo, "r") as arquivo:
            dados = json.load(arquivo)

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

        labelerro1 = QLabel("Email Inválido.")
        labelerro2 = QLabel("Email já é utilizado.")
        labelerro3 = QLabel("A senha digitada não atende aos requisitos de segurança\n do sistema.")
        labelerro4 = QLabel("Senha incorreta.")
        labelerro5 = QLabel("Nome não pode ficar vazio.")
        labelerro1.setStyleSheet("color: red; font-weight: bold; background-color: purple")
        labelerro2.setStyleSheet("color: red; font-weight: bold; background-color: purple")
        labelerro3.setStyleSheet("color: red; font-weight: bold; background-color: purple")
        labelerro4.setStyleSheet("color: red; font-weight: bold; background-color: purple")
        labelerro5.setStyleSheet("color: red; font-weight: bold; background-color: purple")
        labelerro1.hide()
        labelerro2.hide()
        labelerro3.hide()
        labelerro4.hide()
        labelerro5.hide()

        self.janelapri = None

        self.jatem = len(dados["dadosusuario"]["nome"])

        # Crie um widget central para a janela inicial
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Use um layout QVBoxLayout para organizar os widgets
        layout = QVBoxLayout(central_widget)

        def condicoess():
            aux = 0
            if textosenha.text() == textosenha2.text():
                aux += 1
            if len(textosenha.text()) > 5:
                aux += 1
            if any(letra.islower() for letra in textosenha.text()):
                aux += 1
            if any(letra.isupper() for letra in textosenha.text()):
                aux += 1
            if any(letra.isalnum() for letra in textosenha.text()):
                aux += 1
            if any(letra.isnumeric() for letra in textosenha.text()):
                aux += 1
                print(aux)
            if aux == 6:
                return True
            else:
                return False





        def condicoes():
            labelerro1.hide()
            labelerro2.hide()
            labelerro3.hide()
            labelerro4.hide()
            labelerro5.hide()
            self.senhabate = condicoess()
            padraoemail = r"^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$"
            resultadoemail = re.search(padraoemail, textoemail.text())
            if resultadoemail is not None and self.senhabate == True and len(textonome.text()) > 0:
                dados["dadosusuario"]["nome"].append(textonome.text())
                dados["dadosusuario"]["email"].append(textoemail.text())
                dados["dadosusuario"]["senha"].append(textosenha.text())
                with open(nome_arquivo, "w") as arquivo:
                    json.dump(dados, arquivo)
                dialog = QDialog()
                main_layout = QVBoxLayout()
                content_layout = QVBoxLayout()
                button_layout = QVBoxLayout()
                dialog.setWindowTitle("SALVAR NOTA")
                dialog.setWindowIcon(QIcon("imagens/IC.ico"))
                labelavi = QLabel("Nota salva com sucesso!.")
                buttonavi = QPushButton("Ok")
                buttonavi.setFixedSize(100, 30)
                content_layout.addWidget(labelavi)
                labelavi.setStyleSheet("text-align: center")

                button_layout.addWidget(buttonavi)
                button_layout.setAlignment(Qt.AlignmentFlag.AlignBottom)
                button_layout.setContentsMargins(40, 0, 0, 0)

                main_layout.addLayout(content_layout)
                main_layout.addLayout(button_layout)

                buttonavi.clicked.connect(abrirtelapri)
                buttonavi.clicked.connect(dialog.close)

                dialog.setLayout(main_layout)
                dialog.resize(200, 80)
                dialog.setMaximumSize(200, 80)
                dialog.exec()
            if resultadoemail is None:
                labelerro1.show()
            for i in range (len(dados["dadosusuario"]["email"])):
                if dados["dadosusuario"]["email"][i] == textoemail.text():
                    labelerro2.show()
            if self.senhabate == False:
                labelerro3.show()
            if textosenha.text() != textosenha2.text():
                labelerro4.show()
            if len(textonome.text()) < 1:
                labelerro5.show()





        def abrirtelapri():
            if self.janelapri is None:
                self.close()
                self.janelapri = CalendarioApp(self.jatem)  # Crie uma nova instância apenas se ainda não existir
            self.janelapri.show()

        button.clicked.connect(condicoes)

        # Configurar a imagem de fundo da janela usando QLabel
        background_image = QLabel(central_widget)
        background_image.setPixmap(QPixmap("imagens/TI.png"))
        background_image.setGeometry(0, 0, 400, 550)
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
        texto_layout.addWidget(labelerro1)
        texto_layout.addWidget(labelerro2)
        texto_layout.addWidget(labelerro3)
        texto_layout.addWidget(labelerro4)
        texto_layout.addWidget(labelerro5)
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
        self.resize(400, 550)
        self.setMaximumSize(400, 550)

    def closeEvent(self, event):
        from TelaInicial import TelaInicial
        telainicio = TelaInicial()
        telainicio.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    historico = Cadastro()
    historico.show()
    sys.exit(app.exec())