import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Trocar Widget")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout_calendario = QVBoxLayout()
        self.layout_texto = QVBoxLayout()

        self.botao_calendario = QPushButton("Mostrar Calendário")
        self.botao_calendario.clicked.connect(self.mostrar_calendario)

        self.botao_texto = QPushButton("Mostrar Texto")
        self.botao_texto.clicked.connect(self.mostrar_texto)

        self.layout_calendario.addWidget(self.botao_calendario)
        self.layout_texto.addWidget(self.botao_texto)

        self.central_widget.setLayout(self.layout_calendario)

        self.texto = QLabel("Este é um texto de exemplo.")
        self.texto.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout_texto.addWidget(self.texto)

    def mostrar_calendario(self):
        self.central_widget.setLayout(self.layout_calendario)

    def mostrar_texto(self):
        self.central_widget.setLayout(self.layout_texto)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
