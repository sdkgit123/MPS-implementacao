from PyQt6.QtWidgets import QApplication, QCalendarWidget, QHeaderView

app = QApplication([])

calendar = QCalendarWidget()

calendar.setStyleSheet("background-color: red")


calendar.show()

app.exec()

