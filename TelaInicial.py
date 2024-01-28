import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel
from PyQt6.QtCore import Qt, QSize

def main():
    app = QApplication(sys.argv)
    widget = QWidget()
    widget.setMinimumSize(QSize(500, 500))
    widget.setMaximumSize(QSize(500, 500))
    layout = QGridLayout(widget)
    
    # Ajuste o espaçamento entre os itens do layout
    layout.setSpacing(10)  # Ajuste o valor conforme necessário

    label = QLabel("Olá, mundo!")
    label.setStyleSheet("font-size: 18px; font-family: 'Arial'; color: blue;")
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    layout.addWidget(label, 0, 0, 1, 2)  # Posiciona o QLabel na linha 0, coluna 0, com uma ocupação de 1 linha e 2 colunas

    button = QPushButton("Botão")
    button.setMinimumSize(QSize(50, 30))
    layout.addWidget(button, 1, 0, 1, 1)  # Posiciona o QPushButton na linha 1, coluna 0, com uma ocupação de 1 linha e 1 coluna

    otobutton = QPushButton("Outro Botão")
    otobutton.setMinimumSize(QSize(50, 30))
    layout.addWidget(otobutton, 1, 1, 1, 1)  # Posiciona o QPushButton na linha 1, coluna 1, com uma ocupação de 1 linha e 1 coluna

    widget.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
