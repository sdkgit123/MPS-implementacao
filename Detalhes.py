import sys

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QApplication, QHBoxLayout
import json
class Detalhesn(QWidget):
    fechar_det = pyqtSignal()
    def __init__(self, row):
        super().__init__()
        self._closed = False
        nome_arquivo = "dados.json"
        with open(nome_arquivo, "r") as arquivo:
            dados = json.load(arquivo)
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.cor_opcoes = {
            "Reunião": QColor(255, 99, 71),
            "Lembrete": QColor(255, 250, 205),
            "Evento": QColor(0, 255, 255),
            "Tarefa": QColor(152, 251, 152)
        }

        if dados["dadosevento"]["tipo"][row] == "Reunião":
            self.setStyleSheet("background-color: rgb(255, 99, 71);")
        elif dados["dadosevento"]["tipo"][row] == "Lembrete":
            self.setStyleSheet("background-color: rgb(255, 250, 205);")
        elif dados["dadosevento"]["tipo"][row] == "Evento":
            self.setStyleSheet("background-color: rgb(0, 255, 255);")
        elif dados["dadosevento"]["tipo"][row] == "Tarefa":
            self.setStyleSheet("background-color: rgb(152, 251, 152);")

        label = QLabel(f"{dados["dadosevento"]["titulo"][row]}")
        label2 = QLabel(f"Data: {dados["dadosevento"]["data"][row]}")
        label3 = QLabel(f"Tipo: {dados["dadosevento"]["tipo"][row]}")
        label4 = QLabel(f"Hora: {dados["dadosevento"]["horario"][row]}")
        label5 = QLabel(f"Alarme: {dados["dadosevento"]["alarme"][row]}")
        label6 = QLabel(f"Link Videoconferência: {dados["dadosevento"]["link"][row]}")
        layout.addWidget(label)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addWidget(label4)
        layout.addWidget(label5)
        layout.addWidget(label6)


        button = QPushButton("Anotações")
        button2 = QPushButton("Anexos")
        layout.addWidget(button)
        layout.addWidget(button2)

        otolayout = QHBoxLayout()
        button3 = QPushButton("Excluir Evento")
        button4 = QPushButton("Editar Evento")
        otolayout.addWidget(button3)
        otolayout.addWidget(button4)

        layout.addLayout(otolayout)

        self.setWindowTitle("Minha Tela")
        self.resize(500, 500)
        self.setMaximumSize(500, 500)
        self.show()

    def closeEvent(self, event):
        if not self._closed:
            self._closed = True
            self.fechar_det.emit()
            if self.parent():
                self.parent().show()
        event.accept()
