import sys
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemplo de QLineEdit e QPushButton")
        layout = QVBoxLayout(self)

        # Criando um QLineEdit como uma caixa de texto não editável
        self.line_edit = QLineEdit()
        self.line_edit.setReadOnly(True)  # Torna o QLineEdit não editável
        layout.addWidget(self.line_edit)

        # Criando um QPushButton e conectando seu sinal clicked ao slot update_line_edit_text
        self.button = QPushButton("Mulheres peladas")
        self.button.clicked.connect(self.update_line_edit_text)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def update_line_edit_text(self):
        # Atualiza o texto do QLineEdit com o texto do botão clicado
        clicked_button_text = self.sender().text()
        self.line_edit.setText(clicked_button_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
