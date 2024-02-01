import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel

app = QApplication(sys.argv)

label = QLabel("AGENDA")

button = QPushButton("Cadastre-se")

def clicado():
    print("O botão foi clicado!")

otobutton = QPushButton("Fazer Login")

button.clicked.connect(clicado)
otobutton.clicked.connect(clicado)

# Crie uma QMainWindow ao invés de QWidget:
window = QMainWindow()

window.setStyleSheet("window-icon: url(imagens/IC.png);")

# Crie um widget central para a janela
central_widget = QWidget()
window.setCentralWidget(central_widget)

# Use um layout QVBoxLayout para organizar os widgets
layout = QVBoxLayout(central_widget)

# Configurar a imagem de fundo da janela usando QLabel
background_image = QLabel(central_widget)
background_image.setPixmap(QPixmap("imagens/TI.png"))
background_image.setGeometry(0, 0, 400, 500)
background_image.lower()  # Garante que a imagem de fundo esteja atrás dos outros elementos

# Layout para o label
label_layout = QVBoxLayout()
label_layout.addWidget(label)
label_layout.setAlignment(label, Qt.AlignmentFlag.AlignTop)  # Alinhar o label no topo
label_layout.setContentsMargins(90, 100, 0, 0)  # Margens específicas para o layout do label

# Layout para os botões
buttons_layout = QVBoxLayout()
buttons_layout.addWidget(button)
buttons_layout.addWidget(otobutton)
buttons_layout.setAlignment(Qt.AlignmentFlag.AlignBottom)  # Alinhar os botões na parte inferior
buttons_layout.setContentsMargins(145, 0, 0, 100)  # Margens específicas para o layout dos botões
buttons_layout.setSpacing(30)

# Adicione os layouts ao layout principal
layout.addLayout(label_layout)
layout.addLayout(buttons_layout)

# Defina o tamanho do botão:
button.setFixedSize(100, 50)
otobutton.setFixedSize(100, 50)
label.setFixedSize(235, 50)
label.setAutoFillBackground(False)

# Defina o estilo da borda e fundo para os botões
button.setStyleSheet("font-size: 15px; border: 1px solid black; background-color: gray; font-weight: bold;")
otobutton.setStyleSheet("font-size: 15px; border: 1px solid black; background-color: gray; font-weight: bold")

# Defina o estilo do texto da label
label.setStyleSheet("font-size: 50px; text-align: center; color: white; background: rgba(255, 255, 255, 0); font-weight: bold")
window.setWindowIcon(QIcon("imagens\IC.ico"))
window.resize(400, 500)
window.setMaximumSize(400, 500)

window.show()

app.exec()
