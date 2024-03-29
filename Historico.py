import sys
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QIcon, QPixmap, QAction, QFont, QColor, QStandardItem, QStandardItemModel, QBrush, QPalette
from PyQt6.QtWidgets import QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget, QApplication, QDialog, QTableWidget, \
    QTableWidgetItem, QHeaderView, QHBoxLayout, QLineEdit, QItemDelegate, QAbstractItemView
from Agendar import Agenda
from Detalhes import Detalhesn
import json


class Historico(QMainWindow):
    fechar_hist = pyqtSignal()
    def __init__(self, numero):
        super().__init__()
        self._closed = False
        nome_arquivo = "dados.json"

        # Ler o conteúdo do arquivo JSON
        with open(nome_arquivo, "r") as arquivo:
            self.dados = json.load(arquivo)

        self.numeror = numero

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
        self.tableWidget.setRowCount(len(self.dados["dadosevento"]["tipo"]))
        self.tableWidget.setColumnCount(1)

        self.cor_opcoes = {
            "Reunião": QColor(255,99,71),
            "Lembrete": QColor(255,250,205),
            "Evento": QColor(0,255,255),
            "Tarefa": QColor(152,251,152)
        }


        button2 = QPushButton("Adicionar Evento")
        button2.setFixedSize(100, 30)
        button2.clicked.connect(self.mostrar_agenda)

        if len(self.dados["dadosevento"]["tipo"]) == 0:
            widget_transparente = QWidget(self)
            widget_transparente.setGeometry(self.tableWidget.geometry())
            widget_transparente.setStyleSheet("background-color: rgba(0, 0, 0, 0)")  # Define o fundo como transparente
            # Adicionar o widget transparente como um widget filho da janela principal
            widget_transparente.setParent(self)
            # Tornar o widget transparente interceptável para eventos de mouse
            widget_transparente.setMouseTracking(True)
            widget_transparente.setGeometry(0, 80, 800, 300)  # Define o tamanho igual ao da tabela
            # Garantir que o widget transparente esteja na parte superior da pilha de widgets
            widget_transparente.raise_()
            self.tableWidget.setRowCount(1)
            naotem = "Não há notas marcadas."
            item2 = QTableWidgetItem(naotem)  # Criando o item com o texto desejado
            item2.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.tableWidget.setShowGrid(False)
            self.tableWidget.setItem(0, 0, item2)  # Adicionando o widget na primeira linha


        for row in range(len(self.dados["dadosevento"]["tipo"])):
            # Cria o botão para esta linha
            button = QPushButton("Detalhes")
            button.setFixedSize(100, 30)

            # Obtém os dados específicos do evento atual
            titulo = self.dados["dadosevento"]["titulo"][row]
            tipo = self.dados["dadosevento"]["tipo"][row]
            data = self.dados["dadosevento"]["data"][row]
            horario = self.dados["dadosevento"]["horario"][row]

            # Cria o texto do item da tabela com os dados do evento atual
            item_text = f"{titulo} - {tipo}\nData: {data}\nHora: {horario}"
            item = QTableWidgetItem(item_text)

            # Atualiza a cor do item de tabela com base no tipo de evento
            if tipo in self.cor_opcoes:
                item.setBackground(self.cor_opcoes[tipo])

            # Cria o widget personalizado para esta linha
            custom_widget = self.create_custom_widget(button, item, self.cor_opcoes.get(tipo))

            # Conecta o sinal clicked do botão à função handle_detalhes_button_clicked para esta linha
            button.clicked.connect(lambda checked, row=row: self.handle_detalhes_button_clicked(row))

            # Adiciona o widget personalizado à tabela
            self.tableWidget.setCellWidget(row, 0, custom_widget)


        layoutabaixo = QVBoxLayout()
        layoutabaixo.addWidget(button2)
        layoutabaixo.setContentsMargins(330, 0, 0, 0)


        # Aqui você conecta o sinal clicked do botão à função handle_detalhes_button_clicked


        self.tableWidget.setStyleSheet("background-color: #BA55D3;")

        # Ajustando o tamanho das colunas
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tableWidget.verticalHeader().setDefaultSectionSize(100)

        # Escondendo os cabeçalhos
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        layout.addLayout(buscalayout)
        layout.addWidget(self.tableWidget)
        layout.addLayout(layoutabaixo)
        self.janeladetalhe = None

    def handle_detalhes_button_clicked(self, row):
        # Aqui você pode usar o número da linha (row) para determinar qual linha foi clicada
        if self.janeladetalhe is None:
            self.hide()
            self.janeladetalhe = Detalhesn(row)  # Crie uma nova instância apenas se ainda não existir
            self.janeladetalhe.show()
            self.janeladetalhe.fechar_det.connect(self.mostrar_principal2)

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
        
        # Define a cor de fundo da célula diretamente
        if color is not None:
            item.setBackground(color)    
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
        title_action = QAction(f"{self.dados['dadosusuario']['nome'][self.numeror]}", self)
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
        self.agenda = Agenda(self.numeror)
        self.agenda.fechar_agenda.connect(self.mostrar_principal)
        self.agenda.show()

    def mostrar_principal(self):
        self.agenda.close()
        self.show()

    def mostrar_principal2(self):
        self.janeladetalhe.close()
        self.show()
        self.janeladetalhe = None


    def closeEvent(self, event):
        if not self._closed:
            self._closed = True
            self.fechar_hist.emit()
            if self.parent():
                self.parent().show()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela_inicial = Historico(0)
    tela_inicial.show()
    sys.exit(app.exec())