import sys
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QIcon, QPixmap, QAction, QFont, QColor
from PyQt6.QtWidgets import QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget, QApplication, QLineEdit, \
    QHBoxLayout, QComboBox, QDialog, QScrollArea
import json
import re
import validators

class Agenda(QMainWindow):
    fechar_agenda = pyqtSignal()

    def __init__(self):
        super().__init__()
        self._closed = False  # Definindo o atributo 'closed' como False inicialmente
        nome_arquivo = "dados.json"

        # Ler o conteúdo do arquivo JSON
        with open(nome_arquivo, "r") as arquivo:
            self.dados = json.load(arquivo)

        self.setWindowTitle("AGENDAR")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layoutprincipal = QVBoxLayout(central_widget)

        labeldata = QLabel("Para a Data (formato DD/MM/AAAA):")
        labeltipo = QLabel("Tipo da Nota:")
        labelhorario = QLabel("Horário:")
        labelnome = QLabel("Título:")
        labelaalarme = QLabel("Definir Alarme Para:")
        labellink = QLabel("Link Para Reunião:")

        buttona = QPushButton("Adicionar Anotações")
        buttonx = QPushButton("Adicionar Anexos")
        buttonc = QPushButton("Convidar Pessoas")
        buttons = QPushButton("Salvar")

        textodata = QLineEdit(self)
        textohorario = QLineEdit(self)
        textonome = QLineEdit(self)
        textoaalarme = QLineEdit(self)
        textolink = QLineEdit(self)


        combot = QComboBox(self)
        combot.addItem("Reunião")
        combot.addItem("Lembrete")
        combot.addItem("Tarefa")
        combot.addItem("Evento")
        combot.setCurrentIndex(-1)

        background_image = QLabel(central_widget)
        background_image.setPixmap(QPixmap("imagens/TI.png"))
        background_image.setGeometry(0, 0, 800, 600)
        background_image.lower()  # Garanta que a imagem de fundo esteja atrás dos outros elementos

        # Layout para o label
        label1_layout = QHBoxLayout()
        label1_layout.addWidget(labeldata)
        label1_layout.addWidget(textodata)
        label1_layout.setAlignment(labeldata, Qt.AlignmentFlag.AlignTop)  # Alinhe o label no topo
        label1_layout.setContentsMargins(0, 0, 10, 0)
        labeldata.setFixedSize(270, 50)
        textodata.setFixedSize(490, 30)
        labeldata.setStyleSheet("font-size: 15px; color: white; font-weight: bold")

        label2_layout = QHBoxLayout()
        label2_layout.addWidget(labeltipo)
        label2_layout.addWidget(combot)
        label2_layout.setAlignment(labeldata, Qt.AlignmentFlag.AlignTop)  # Alinhe o label no topo
        label2_layout.setContentsMargins(0, 0, 250, 0)
        labeltipo.setFixedSize(120, 50)
        combot.setFixedSize(400, 30)
        labeltipo.setStyleSheet("font-size: 15px; color: white; font-weight: bold")

        label3_layout = QHBoxLayout()
        label3_layout.addWidget(labelhorario)
        label3_layout.addWidget(textohorario)
        label3_layout.setAlignment(labeldata, Qt.AlignmentFlag.AlignTop)  # Alinhe o label no topo
        label3_layout.setContentsMargins(0, 0, 310, 0)
        labelhorario.setFixedSize(60, 50)
        textohorario.setFixedSize(400, 30)
        labelhorario.setStyleSheet("font-size: 15px; color: white; font-weight: bold")

        label4_layout = QHBoxLayout()
        label4_layout.addWidget(labelnome)
        label4_layout.addWidget(textonome)
        label4_layout.setAlignment(labeldata, Qt.AlignmentFlag.AlignTop)  # Alinhe o label no topo
        label4_layout.setContentsMargins(0, 0, 320, 0)
        labelnome.setFixedSize(50, 50)
        textonome.setFixedSize(400, 30)
        labelnome.setStyleSheet("font-size: 15px; color: white; font-weight: bold")

        label5_layout = QHBoxLayout()
        label5_layout.addWidget(labelaalarme)
        label5_layout.addWidget(textoaalarme)
        label5_layout.setAlignment(labeldata, Qt.AlignmentFlag.AlignTop)  # Alinhe o label no topo
        label5_layout.setContentsMargins(0, 0, 220, 0)
        labelaalarme.setFixedSize(150, 50)
        textoaalarme.setFixedSize(400, 30)
        labelaalarme.setStyleSheet("font-size: 15px; color: white; font-weight: bold")

        label6_layout = QHBoxLayout()
        label6_layout.addWidget(labellink)
        label6_layout.addWidget(textolink)
        label6_layout.setAlignment(labeldata, Qt.AlignmentFlag.AlignTop)  # Alinhe o label no topo
        label6_layout.setContentsMargins(0, 0, 230, 0)
        labellink.setFixedSize(140, 50)
        textolink.setFixedSize(400, 30)
        labellink.setStyleSheet("font-size: 15px; color: white; font-weight: bold")

        # Layout para os botões
        buttons_layout = QVBoxLayout()
        buttons_layout.addWidget(buttona)
        buttons_layout.addWidget(buttonx)
        buttons_layout.addWidget(buttonc)
        buttons_layout.setAlignment(Qt.AlignmentFlag.AlignBottom)  # Alinhe os botões na parte inferior
        buttons_layout.setContentsMargins(0, 0, 0, 0)  # Margens específicas para o layout dos botões
        buttons_layout.setSpacing(20)
        buttona.setFixedSize(130, 40)
        buttonx.setFixedSize(130, 40)
        buttonc.setFixedSize(130, 40)

        layout_erros = QVBoxLayout()
        dataerro = QLabel("Data: Campo Inválido")
        nomeerro = QLabel("Título: Campo Inválido")
        tipoerro = QLabel("Tipo: Campo Inválido")
        horaerro = QLabel("Horário: Formato Inválido")
        alarmeerro = QLabel("Alarme: Formato Inválido")
        linkerro = QLabel("Link Videoconferência: Formato Inválido")
        dataerro.setStyleSheet("color: red; font-weight: bold; background-color: purple")
        nomeerro.setStyleSheet("color: red; font-weight: bold; background-color: purple")
        tipoerro.setStyleSheet("color: red; font-weight: bold; background-color: purple")
        horaerro.setStyleSheet("color: red; font-weight: bold; background-color: purple")
        alarmeerro.setStyleSheet("color: red; font-weight: bold; background-color: purple")
        linkerro.setStyleSheet("color: red; font-weight: bold; background-color: purple")
        layout_erros.addWidget(dataerro)
        layout_erros.addWidget(nomeerro)
        layout_erros.addWidget(tipoerro)
        layout_erros.addWidget(horaerro)
        layout_erros.addWidget(alarmeerro)
        layout_erros.addWidget(linkerro)
        dataerro.hide()
        nomeerro.hide()
        tipoerro.hide()
        horaerro.hide()
        alarmeerro.hide()
        linkerro.hide()

        layoutlayout = QHBoxLayout()
        layoutlayout.addLayout(buttons_layout)
        layoutlayout.addLayout(layout_erros)
        layoutlayout.setAlignment(Qt.AlignmentFlag.AlignLeft)


        button_layout = QVBoxLayout()
        button_layout.addWidget(buttons)
        button_layout.setAlignment(Qt.AlignmentFlag.AlignBottom)  # Alinhe os botões na parte inferior
        button_layout.setContentsMargins(300, 0, 0, 10)  # Margens específicas para o layout dos botões
        button_layout.setSpacing(30)
        buttons.setFixedSize(130, 40)




        labeldata.setAutoFillBackground(False)

        # Adicione os layouts ao layout principal
        layoutprincipal.addLayout(label1_layout)
        layoutprincipal.addLayout(label2_layout)
        layoutprincipal.addLayout(label3_layout)
        layoutprincipal.addLayout(label4_layout)
        layoutprincipal.addLayout(label5_layout)
        layoutprincipal.addLayout(label6_layout)
        layoutprincipal.addLayout(layoutlayout)
        layoutprincipal.addLayout(button_layout)

        self.setWindowIcon(QIcon("imagens/IC.ico"))
        self.resize(800, 600)
        self.setMaximumSize(800, 600)
        self.create_toolbar()

        self.hist = None






        def salvar():
            self.erros = 0
            regex = r"^\d{1,2}/\d{1,2}/\d{4}$"
            self.resultadodata = re.search(regex, textodata.text())
            padrao_horario = r'^([01]?[0-9]|2[0-3]):[0-5][0-9]$'
            self.resultadohorario = re.search(padrao_horario, textohorario.text())
            self.resultadoalarme = re.search(padrao_horario, textoaalarme.text())
            dataerro.hide()
            nomeerro.hide()
            tipoerro.hide()
            horaerro.hide()
            alarmeerro.hide()
            linkerro.hide()


            if len(textohorario.text()) != 0 and self.resultadohorario is None:
                self.erros += 1
            if len(textoaalarme.text()) != 0 and self.resultadoalarme is None:
                self.erros += 1
            if len(textolink.text()) != 0 and not validators.url(textolink.text()):
                self.erros += 1
            if len(textodata.text()) == 0 or self.resultadodata is None:
                self.erros += 1
            if len(textonome.text()) == 0:
                self.erros += 1
            if len(combot.currentText()) == 0:
                self.erros += 1

            if self.erros == 0:
                self.itemselecionado = combot.currentText()
                self.dados["dadosevento"]["tipo"].append(self.itemselecionado)
                self.dados["dadosevento"]["data"].append(textodata.text())
                self.dados["dadosevento"]["horario"].append(textohorario.text())
                self.dados["dadosevento"]["titulo"].append(textonome.text())
                self.dados["dadosevento"]["alarme"].append(textoaalarme.text())
                self.dados["dadosevento"]["link"].append(textolink.text())
                with open(nome_arquivo, "w") as arquivo:
                    json.dump(self.dados, arquivo)
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

                buttonavi.clicked.connect(self.close)
                buttonavi.clicked.connect(dialog.close)

                dialog.setLayout(main_layout)
                dialog.resize(200, 80)
                dialog.setMaximumSize(200, 80)
                dialog.exec()


            else:
                if len(textohorario.text()) != 0 and self.resultadohorario is None:
                    horaerro.show()
                if len(textoaalarme.text()) != 0 and self.resultadoalarme is None:
                    alarmeerro.show()
                if len(textodata.text()) == 0 or self.resultadodata is None:
                    dataerro.show()
                if len(textolink.text()) != 0 and not validators.url(textolink.text()):
                    linkerro.show()
                if len(textonome.text()) == 0:
                    nomeerro.show()
                if len(combot.currentText()) == 0:
                    tipoerro.show()

        buttons.clicked.connect(salvar)


        def naoa():
            dialog = QDialog()
            main_layout = QVBoxLayout()
            content_layout = QVBoxLayout()
            button_layout = QVBoxLayout()
            dialog.setWindowTitle("ADICIONAR ANOTAÇÕES")
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
        buttona.clicked.connect(naoa)
        def naox():
            dialog = QDialog()
            main_layout = QVBoxLayout()
            content_layout = QVBoxLayout()
            button_layout = QVBoxLayout()
            dialog.setWindowTitle("ADICIONAR ANEXOS")
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
        buttonx.clicked.connect(naox)
        def naoc():
            dialog = QDialog()
            main_layout = QVBoxLayout()
            content_layout = QVBoxLayout()
            button_layout = QVBoxLayout()
            dialog.setWindowTitle("ADICIONAR CONVIDADOS")
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
        buttonc.clicked.connect(naoc)

    def mostrar_agenda(self):
        dialog = QDialog()
        main_layout = QVBoxLayout()
        content_layout = QVBoxLayout()
        button_layout = QVBoxLayout()
        dialog.setWindowTitle("AGENDAR")
        dialog.setWindowIcon(QIcon("imagens/IC.ico"))
        labelavi = QLabel("Você já está em Agendar.")
        buttonavi = QPushButton("Fechar")
        buttonavi.setFixedSize(100, 30)
        content_layout.addWidget(labelavi)
        content_layout.setContentsMargins(25, 0, 0, 0)

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

    def naoac(self):
        dialog = QDialog()
        main_layout = QVBoxLayout()
        content_layout = QVBoxLayout()
        button_layout = QVBoxLayout()
        dialog.setWindowTitle("AGENDA DE CONTATOS")
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

    def naocn(self):
        dialog = QDialog()
        main_layout = QVBoxLayout()
        content_layout = QVBoxLayout()
        button_layout = QVBoxLayout()
        dialog.setWindowTitle("CONVITES")
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

    def naocf(self):
        dialog = QDialog()
        main_layout = QVBoxLayout()
        content_layout = QVBoxLayout()
        button_layout = QVBoxLayout()
        dialog.setWindowTitle("CONFIGURAÇÕES")
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

    def create_toolbar(self):
        action = QAction("Agendar", self)
        action2 = QAction("Ver Agenda", self)
        action3 = QAction("Agenda de Contatos", self)
        action4 = QAction("Convites", self)
        action5 = QAction("Configurações", self)
        menu = self.menuBar()
        file_menu = menu.addMenu("File")
        title_action = QAction("Fulano de Tal", self)
        menu.setStyleSheet("font-family: Arial; font-size: 20pt; font-weight: bold; background-color: #993399; color: "
                           "#ffffff")
        title_action.setEnabled(False)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        action.setFont(font)
        action2.setFont(font)
        action3.setFont(font)
        action4.setFont(font)
        action5.setFont(font)
        file_menu.addAction(action)
        file_menu.addAction(action2)
        file_menu.addAction(action3)
        file_menu.addAction(action4)
        file_menu.addAction(action5)
        icon_path = "imagens/MN.png"  # Certifique-se de fornecer o caminho correto para o ícone
        file_menu.setIcon(QIcon(icon_path))
        menu.setMinimumHeight(30)
        action.triggered.connect(self.mostrar_agenda)
        action2.triggered.connect(self.mostrar_historico)
        action3.triggered.connect(self.naoac)
        action4.triggered.connect(self.naocn)
        action5.triggered.connect(self.naocf)
        menu.addMenu(file_menu)
        menu.addAction(title_action)
    def mostrar_historico(self):
        from Historico import Historico
        self.hide()
        self.hist = Historico()
        self.hist.fechar_hist.connect(self.mostrar_principal2)
        self.hist.show()

    def mostrar_principal2(self):
        self.hist.close()
        self.show()

    def closeEvent(self, event):
        if not self._closed:
            self._closed = True
            self.fechar_agenda.emit()
            if self.parent():
                self.parent().show()
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    tela_inicial = Agenda()
    tela_inicial.show()
    sys.exit(app.exec())

