import sys
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QIcon, QPixmap, QAction, QFont
from PyQt6.QtWidgets import QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget, QApplication

class Agenda(QMainWindow):
    fechar_agenda = pyqtSignal()

    def __init__(self):
        super().__init__()
        self._closed = False  # Definindo o atributo 'closed' como False inicialmente

        self.setWindowTitle("AGENDAR")

        labeld = QLabel("Para a Data:")
        labelt = QLabel("Tipo do Evento:")
        labelh = QLabel("Horário:")
        labeln = QLabel("Título:")
        labela = QLabel("Definir Alarme Para:")
        

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
        background_image.setGeometry(0, 0, 800, 500)
        background_image.lower()  # Garanta que a imagem de fundo esteja atrás dos outros elementos

        # Layout para o label
        label_layout = QVBoxLayout()
        label_layout.addWidget(labeld)
        label_layout.setAlignment(labeld, Qt.AlignmentFlag.AlignTop)  # Alinhe o label no topo
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
        labeld.setFixedSize(235, 50)
        labeld.setAutoFillBackground(False)

        # Adicione os layouts ao layout principal
        layout.addLayout(label_layout)
        layout.addLayout(buttons_layout)

        self.setWindowIcon(QIcon("imagens/IC.ico"))
        self.resize(800, 500)
        self.setMaximumSize(800, 500)
        self.create_toolbar()

    def create_toolbar(self):
        action = QAction("Agendar", self)
        action2 = QAction("Bueno", self)
        menu = self.menuBar()
        file_menu = menu.addMenu("File")
        title_action = QAction("Fulano de Tal", self)
        menu.setStyleSheet("font-family: Arial; font-size: 20pt; font-weight: bold; background-color: #993399; color: #ffffff")
        title_action.setEnabled(False)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        action.setFont(font)
        action2.setFont(font)
        file_menu.addAction(action)
        file_menu.addAction(action2)
        icon_path = "imagens/MN.png"  # Certifique-se de fornecer o caminho correto para o ícone
        file_menu.setIcon(QIcon(icon_path))
        menu.setMinimumHeight(30)
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

