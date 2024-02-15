import sys

from PyQt5.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QCalendarWidget, QVBoxLayout, QPushButton, QWidget, QHBoxLayout, \
    QLabel, QStackedWidget, QGridLayout


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

        self.setWindowTitle("Calendário")
        self.setGeometry(100, 100, 400, 300)

        # Criando um widget central para conter o layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Criando um layout vertical
        layout_principal = QVBoxLayout(central_widget)

        # Criando um layout horizontal para os botões
        layout_botoes = QHBoxLayout()


        self.menu_lateral = QWidget()
        self.menu_lateral.setMinimumWidth(100)  # Defina a largura mínima do menu lateral
        self.menu_lateral_layout = QVBoxLayout(self.menu_lateral)
        self.menu_lateral_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)  # Alinhe os elementos no topo do menu lateral

        # Adicione elementos ao menu lateral
        self.label_menu = QLabel("Menu")
        self.botao_opcao1 = QPushButton("Opção 1")
        self.botao_opcao2 = QPushButton("Opção 2")
        self.menu_lateral_layout.addWidget(self.label_menu)
        self.menu_lateral_layout.addWidget(self.botao_opcao1)
        self.menu_lateral_layout.addWidget(self.botao_opcao2)

        # Inicialmente, o menu lateral está oculto
        self.menu_lateral.setVisible(False)

        # Botão para mostrar/ocultar o menu lateral
        botaomenul = QPushButton("=")
        botaomenul.clicked.connect(self.toggle_menu_lateral)

        # Adiciona o menu lateral à esquerda da janela
        layout_principal.addWidget(self.menu_lateral)
        layout_principal.addWidget(botaomenul, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        # Adicionando um botão anterior ao layout de botões
        botao_antes = QPushButton("<<")
        layout_botoes.addWidget(botao_antes)

        self.botao_anomes = QPushButton("")
        layout_botoes.addWidget(self.botao_anomes)

        # Adicionando um botão posterior ao layout de botões
        botao_depois = QPushButton(">>")
        layout_botoes.addWidget(botao_depois)

        layout_principal.addLayout(layout_botoes)

        # Criando um QStackedWidget para alternar entre calendário e texto
        self.stacked_widget = QStackedWidget()
        layout_principal.addWidget(self.stacked_widget)

        # Adicionando o widget de calendário ao QStackedWidget
        self.calendario_widget = QCalendarWidget()
        self.stacked_widget.addWidget(self.calendario_widget)

        # Criando um QWidget para conter a grade de botões
        self.grid_layout = QGridLayout(self.widget_grid)

        # Criar e adicionar botões à matriz de 4x3
        for row in range(4):
            for col in range(3):
                button = QPushButton(f"{listames[row][col]}")
                self.grid_layout.addWidget(button, row, col)
                button.setFixedSize(90,90)
                self.grid_layout.setContentsMargins(20,20,20,20)
                button.clicked.connect(self.botao_clicado)


        self.stacked_widget.addWidget(self.widget_grid)

        # Conectando os botões aos métodos correspondentes
        botao_antes.clicked.connect(self.voltar_um_mes)
        botao_depois.clicked.connect(self.avancar_um_mes)
        self.botao_anomes.clicked.connect(self.toggle_widget)

        # Configurações adicionais para o calendário
        self.calendario_widget.setVerticalHeaderFormat(QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader)
        self.calendario_widget.setNavigationBarVisible(False)

        self.exibindo_calendario = True

        self.atualizar_mes()

        self.resize(400, 500)
        self.setMaximumSize(400, 500)

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

    def toggle_menu_lateral(self):
        self.menu_lateral.setVisible(not self.menu_lateral.isVisible())

def main():
    app = QApplication(sys.argv)
    window = CalendarioApp()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
