import sys
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QIcon, QPixmap, QAction, QFont
from PyQt6.QtWidgets import QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget, QApplication, QLineEdit, \
    QHBoxLayout, QComboBox, QDialog


class Agenda(QMainWindow):
    fechar_agenda = pyqtSignal()

    def __init__(self):
        super().__init__()
        self._closed = False  # Definindo o atributo 'closed' como False inicialmente

        self.setWindowTitle("AGENDAR")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layoutprincipal = QVBoxLayout(central_widget)

        labeld = QLabel("Para a Data (formato DD/MM/AA ou DD/MM/AAAA):")
        labelt = QLabel("Tipo do Evento:")
        labelh = QLabel("Horário:")
        labeln = QLabel("Título:")
        labela = QLabel("Definir Alarme Para:")
        labelr = QLabel("Link Para Reunião:")

        buttona = QPushButton("Adicionar Anotações")
        buttonx = QPushButton("Adicionar Anexos")
        buttonc = QPushButton("Convidar Pessoas")
        buttons = QPushButton("Salvar")

        textod = QLineEdit(self)
        textoh = QLineEdit(self)
        texton = QLineEdit(self)
        textoa = QLineEdit(self)
        textor = QLineEdit(self)

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
        label1_layout.addWidget(labeld)
        label1_layout.addWidget(textod)
        label1_layout.setAlignment(labeld, Qt.AlignmentFlag.AlignTop)  # Alinhe o label no topo
        label1_layout.setContentsMargins(0, 0, 10, 0)
        labeld.setFixedSize(390, 50)
        textod.setFixedSize(370, 30)
        labeld.setStyleSheet("font-size: 15px; color: white; font-weight: bold")

        label2_layout = QHBoxLayout()
        label2_layout.addWidget(labelt)
        label2_layout.addWidget(combot)
        label2_layout.setAlignment(labeld, Qt.AlignmentFlag.AlignTop)  # Alinhe o label no topo
        label2_layout.setContentsMargins(0, 0, 250, 0)
        labelt.setFixedSize(120, 50)
        combot.setFixedSize(400, 30)
        labelt.setStyleSheet("font-size: 15px; color: white; font-weight: bold")

        label3_layout = QHBoxLayout()
        label3_layout.addWidget(labelh)
        label3_layout.addWidget(textoh)
        label3_layout.setAlignment(labeld, Qt.AlignmentFlag.AlignTop)  # Alinhe o label no topo
        label3_layout.setContentsMargins(0, 0, 310, 0)
        labelh.setFixedSize(60, 50)
        textoh.setFixedSize(400, 30)
        labelh.setStyleSheet("font-size: 15px; color: white; font-weight: bold")

        label4_layout = QHBoxLayout()
        label4_layout.addWidget(labeln)
        label4_layout.addWidget(texton)
        label4_layout.setAlignment(labeld, Qt.AlignmentFlag.AlignTop)  # Alinhe o label no topo
        label4_layout.setContentsMargins(0, 0, 320, 0)
        labeln.setFixedSize(50, 50)
        texton.setFixedSize(400, 30)
        labeln.setStyleSheet("font-size: 15px; color: white; font-weight: bold")

        label5_layout = QHBoxLayout()
        label5_layout.addWidget(labela)
        label5_layout.addWidget(textoa)
        label5_layout.setAlignment(labeld, Qt.AlignmentFlag.AlignTop)  # Alinhe o label no topo
        label5_layout.setContentsMargins(0, 0, 220, 0)
        labela.setFixedSize(150, 50)
        textoa.setFixedSize(400, 30)
        labela.setStyleSheet("font-size: 15px; color: white; font-weight: bold")

        label6_layout = QHBoxLayout()
        label6_layout.addWidget(labelr)
        label6_layout.addWidget(textor)
        label6_layout.setAlignment(labeld, Qt.AlignmentFlag.AlignTop)  # Alinhe o label no topo
        label6_layout.setContentsMargins(0, 0, 230, 0)
        labelr.setFixedSize(140, 50)
        textor.setFixedSize(400, 30)
        labelr.setStyleSheet("font-size: 15px; color: white; font-weight: bold")

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

        button_layout = QVBoxLayout()
        button_layout.addWidget(buttons)
        button_layout.setAlignment(Qt.AlignmentFlag.AlignBottom)  # Alinhe os botões na parte inferior
        button_layout.setContentsMargins(300, 0, 0, 10)  # Margens específicas para o layout dos botões
        button_layout.setSpacing(30)
        buttons.setFixedSize(130, 40)



        labeld.setAutoFillBackground(False)

        # Adicione os layouts ao layout principal
        layoutprincipal.addLayout(label1_layout)
        layoutprincipal.addLayout(label2_layout)
        layoutprincipal.addLayout(label3_layout)
        layoutprincipal.addLayout(label4_layout)
        layoutprincipal.addLayout(label5_layout)
        layoutprincipal.addLayout(label6_layout)
        layoutprincipal.addLayout(buttons_layout)
        layoutprincipal.addLayout(button_layout)

        self.setWindowIcon(QIcon("imagens/IC.ico"))
        self.resize(800, 600)
        self.setMaximumSize(800, 600)
        self.create_toolbar()

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
        action3.triggered.connect(self.naoac)
        action4.triggered.connect(self.naocn)
        action5.triggered.connect(self.naocf)
        menu.addMenu(file_menu)
        menu.addAction(title_action)


    def closeEvent(self, event):
        if not self._closed:
            self._closed = True
            self.fechar_agenda.emit()
            if self.parent():
                self.parent().show()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela_inicial = Agenda()
    tela_inicial.show()
    sys.exit(app.exec())

