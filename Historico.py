import sys
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QIcon, QPixmap, QAction, QFont, QColor, QStandardItem, QStandardItemModel, QBrush
from PyQt6.QtWidgets import QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget, QApplication, QDialog, QTableWidget, \
    QTableWidgetItem, QHeaderView, QHBoxLayout, QLineEdit
from Agendar import Agenda


class Historico(QMainWindow):
    fechar_hist = pyqtSignal()
    def __init__(self):
        super().__init__()
        self._closed = False
        self.tipo = ["Reunião", "Lembrete", "Tarefa", "Evento", "", "", "", ""]
        self.data = ["14/03/24", "20/02/2024", "30/02/3078", "40/93/3856", "", "", "", ""]
        self.horario = ["20:00", " ", " ", "seilar", "", "", "", ""]
        self.titulo = ["Niver do Daddy", "A Manu Peida", "O dia que eu vou gostar de homi", "horse", "", "", "", ""]

        self.setWindowTitle("AGENDA")
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Use um layout QVBoxLayout para organizar os widgets
        layout = QVBoxLayout(central_widget)

        # Configurar a imagem de fundo da janela usando QLabel
        background_image = QLabel(central_widget)
        background_image.setPixmap(QPixmap("imagens/TI.png"))
        background_image.setGeometry(0, 0, 800, 500)
        background_image.lower()
        self.setWindowIcon(QIcon("imagens/IC.ico"))
        self.resize(800, 500)
        self.setMaximumSize(800, 500)
        self.create_toolbar()

        buscalayout = QHBoxLayout()
        busca = QLabel("Buscar Nota:")
        busca.setStyleSheet("background-color: #BA55D3; font-weight: bold")
        busca.setFixedSize(100,30)
        buscat = QLineEdit(self)
        buscat.setFixedSize(670, 30)
        buscalayout.addWidget(busca)
        buscalayout.addWidget(buscat)

        # Criando uma tabela QTableWidget
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(len(self.tipo))
        self.tableWidget.setColumnCount(1)
        button = QPushButton("Detalhes")

        self.cor_opcoes = {
            "Reunião": QColor(255, 0, 0),
            "Lembrete": QColor(255, 255, 0),
            "Evento": QColor(0, 0, 255),
            "Tarefa": QColor(50, 205, 50)
        }

        for row in range(len(self.tipo)):
            # Cria o botão
            button = QPushButton("Detalhes")
            button.setFixedSize(100,30)

            item_text = f"{self.titulo[row]} - {self.tipo[row]}\nData: {self.data[row]}\nHora: {self.horario[row]}"
            item = QTableWidgetItem(item_text)

            # Atualizar a cor do item de tabela
            if self.tipo[row] in self.cor_opcoes:
                item.setBackground(self.cor_opcoes[self.tipo[row]])

            # Cria o widget personalizado
            custom_widget = self.create_custom_widget(button, item, self.cor_opcoes.get(self.tipo[row]))

            # Adiciona o widget personalizado à tabela
            self.tableWidget.setCellWidget(row, 0, custom_widget)




        self.tableWidget.setStyleSheet("background-color: #BA55D3;")

        # Ajustando o tamanho das colunas
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tableWidget.verticalHeader().setDefaultSectionSize(100)

        # Escondendo os cabeçalhos
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        layout.addLayout(buscalayout)
        layout.addWidget(self.tableWidget)

    def create_custom_widget(self, button, item, color):
        custom_widget = QWidget()
        layout = QVBoxLayout(custom_widget)
        buttonlayout = QVBoxLayout()
        buttonlayout.addWidget(button)
        buttonlayout.setContentsMargins(325, 0, 0, 0)
        # Adicionando o QTableWidgetItem encapsulado em um QLabel
        label = QLabel()
        label.setText(item.text())
        layout.addWidget(label)
        layout.addLayout(buttonlayout)
        if color is not None:
            custom_widget.setStyleSheet(f"background-color: {color.name()}")
        return custom_widget

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
        menu.setStyleSheet(
            "font-family: Arial; font-size: 20pt; font-weight: bold; background-color: #993399; color: "
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
        dialog = QDialog()
        main_layout = QVBoxLayout()
        content_layout = QVBoxLayout()
        button_layout = QVBoxLayout()
        dialog.setWindowTitle("VER AGENDA")
        dialog.setWindowIcon(QIcon("imagens/IC.ico"))
        labelavi = QLabel("Você já está em Ver Agenda.")
        buttonavi = QPushButton("Fechar")
        buttonavi.setFixedSize(100, 30)
        content_layout.addWidget(labelavi)
        content_layout.setContentsMargins(16, 0, 0, 0)

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

    def mostrar_agenda(self):
        self.hide()
        self.agenda = Agenda()
        self.agenda.fechar_agenda.connect(self.mostrar_principal)
        self.agenda.show()

    def mostrar_principal(self):
        self.agenda.close()
        self.show()

    def closeEvent(self, event):
        if not self._closed:
            self._closed = True
            self.fechar_hist.emit()
            if self.parent():
                self.parent().show()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela_inicial = Historico()
    tela_inicial.show()
    sys.exit(app.exec())