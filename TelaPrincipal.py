import sys
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QIcon, QPixmap, QAction, QFont
from PyQt6.QtWidgets import QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget, QApplication, QHBoxLayout, \
    QStackedWidget, QCalendarWidget, QGridLayout, QDialog
from Agendar import Agenda

class CalendarioApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.agenda = None

        self.widget_grid = QWidget()

        listames = [['Janeiro', 'Fevereiro', 'Março'],
                    ['Abril', 'Maio', 'Junho'],
                    ['Julho', 'Agosto', 'Setembro'],
                    ['Outubro', 'Novembro', 'Dezembro']]

        self.numeromes = [[1, 2, 3],
                          [4, 5, 6],
                          [7, 8, 9],
                          [10, 11, 12]]

        self.janelaagenda = None

        self.setWindowTitle("TELA PRINCIPAL")
        self.setGeometry(100, 100, 800, 500)  # Definindo uma largura maior para a janela
        icon_path = "imagens/IC.ico"  # Certifique-se de fornecer o caminho correto para o ícone
        CalendarioApp.setWindowIcon(self, QIcon(icon_path))
        # Criando um widget central para conter o layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        background_image = QLabel(central_widget)
        background_image.setPixmap(QPixmap("imagens/TI.png"))
        background_image.setGeometry(0, 0, 800, 500)
        background_image.lower()

        # Criando um layout vertical
        layout_principal = QVBoxLayout(central_widget)

        # Criando um layout horizontal para os botões e menu lateral
        layout_horizontal = QHBoxLayout()

        # Adiciona o layout horizontal ao layout principal
        layout_principal.addLayout(layout_horizontal)

        # Criando um QStackedWidget para alternar entre calendário e texto
        self.stacked_widget = QStackedWidget()
        layout_principal.addWidget(self.stacked_widget)

        # Adicionando o widget de calendário ao QStackedWidget
        self.calendario_widget = QCalendarWidget()
        self.stacked_widget.addWidget(self.calendario_widget)
        self.calendario_widget.setStyleSheet("background-color: #b34db2; font-weight: bold")
        self.calendario_widget.setGridVisible(True)
        # Criando um QWidget para conter a grade de botões
        self.widget_grid = QWidget()
        self.grid_layout = QGridLayout(self.widget_grid)

        # Criar e adicionar botões à matriz de 4x3
        for row in range(4):
            for col in range(3):
                button = QPushButton(f"{listames[row][col]}")
                self.grid_layout.addWidget(button, row, col)
                button.setFixedSize(100, 100)
                self.grid_layout.setContentsMargins(10, 10, 10, 10)
                button.setStyleSheet("background-color: #b34db2; color: white; font-weight: bold")
                button.clicked.connect(self.botao_clicado)

        self.stacked_widget.addWidget(self.widget_grid)

        # Conectando os botões aos métodos correspondentes
        self.botao_anomes = QPushButton("")
        self.botao_anomes.clicked.connect(self.toggle_widget)
        botao_antes = QPushButton("<<")
        botao_antes.clicked.connect(self.voltar_um_mes)
        botao_depois = QPushButton(">>")
        botao_depois.clicked.connect(self.avancar_um_mes)

        # Adiciona os botões ao layout horizontal
        layout_horizontal.addWidget(botao_antes)
        layout_horizontal.addWidget(self.botao_anomes)
        layout_horizontal.addWidget(botao_depois)
        central_widget.setLayout(layout_principal)

        # Configurações adicionais para o calendário
        self.calendario_widget.setVerticalHeaderFormat(QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader)
        self.calendario_widget.setNavigationBarVisible(False)

        self.exibindo_calendario = True

        self.atualizar_mes()

        self.resize(800, 500)  # Redimensiona a janela
        self.setMaximumSize(800, 500)

        self.create_toolbar()
        self.agenda = None

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

    def voltar_um_mes(self):
        if self.exibindo_calendario:
            self.calendario_widget.showPreviousMonth()
            self.atualizar_mes()
        else:
            self.calendario_widget.showPreviousYear()
            self.atualizar_mes()

    def avancar_um_mes(self):
        if self.exibindo_calendario:
            self.calendario_widget.showNextMonth()
            self.atualizar_mes()
        else:
            self.calendario_widget.showNextYear()
            self.atualizar_mes()

    def atualizar_mes(self):
        if self.exibindo_calendario:
            ano = self.calendario_widget.yearShown()
            mes = self.calendario_widget.monthShown()
            self.botao_anomes.setText(f"{ano}/{mes:02d}")
        else:
            ano = self.calendario_widget.yearShown()
            self.botao_anomes.setText(f"{ano}")

    def toggle_widget(self):
            # Método para alternar entre o calendário e a grade de botões
        if self.exibindo_calendario:
            self.stacked_widget.setCurrentWidget(self.widget_grid)
            ano = self.calendario_widget.yearShown()
            self.botao_anomes.setText(str(ano))
        else:
            self.stacked_widget.setCurrentWidget(self.calendario_widget)
            ano = self.calendario_widget.yearShown()
            mes = self.calendario_widget.monthShown()
            self.botao_anomes.setText(f"{ano}/{mes:02d}")

        self.exibindo_calendario = not self.exibindo_calendario

    def botao_clicado(self):
        sender = self.sender()  # Obter o botão que enviou o sinal
        for row in range(4):
            for col in range(3):
                    # Verificar se o objeto do botão na posição (row, col) é o mesmo que o sender
                if self.grid_layout.itemAtPosition(row, col).widget() == sender:
                    ano = self.calendario_widget.yearShown()
                    self.calendario_widget.setSelectedDate(self.calendario_widget.selectedDate().addYears(
                        ano - self.calendario_widget.selectedDate().year()).addMonths(self.numeromes[row][col] - 2))
                    self.stacked_widget.setCurrentWidget(self.calendario_widget)
                    self.toggle_widget()
                    return
    def mostrar_agenda(self):
        self.hide()
        self.agenda = Agenda()
        self.agenda.fechar_agenda.connect(self.mostrar_principal)
        self.agenda.show()

    def mostrar_principal(self):
        self.agenda.close()
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    tela_inicial = CalendarioApp()
    tela_inicial.show()
    sys.exit(app.exec())


