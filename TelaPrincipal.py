import sys
from PyQt6.QtGui import QAction, QIcon, QPixmap, QFont
from PyQt6.QtWidgets import QApplication, QMainWindow, QCalendarWidget, QVBoxLayout, QPushButton, QWidget, QHBoxLayout, \
    QStackedWidget, QGridLayout, QLabel
from Agendar import Agenda

class CalendarioApp(QMainWindow):
    def __init__(self):
        super().__init__()

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

        self.setWindowTitle("Calendário")
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
        self.calendario_widget.setStyleSheet("background-color: #b34db2")
        self.calendario_widget.setGridVisible(True)
        # Criando um QWidget para conter a grade de botões
        self.widget_grid = QWidget()
        self.grid_layout = QGridLayout(self.widget_grid)

        # Criar e adicionar botões à matriz de 4x3
        for row in range(4):
            for col in range(3):
                button = QPushButton(f"{listames[row][col]}")
                self.grid_layout.addWidget(button, row, col)
                button.setFixedSize(90, 90)
                self.grid_layout.setContentsMargins(20, 20, 20, 20)
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
        action.triggered.connect(self.abrir_agendar)
        menu.addMenu(file_menu)
        menu.addAction(title_action)

    def abrir_agendar(self):
        if self.janelaagenda is None:
            self.hide()
            self.janelaagenda = Agenda()  # Crie uma nova instância apenas se ainda não existir
            self.janelaagenda.show()

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


def main():
    app = QApplication(sys.argv)
    window = CalendarioApp()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()