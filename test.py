import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QPushButton

app = QApplication(sys.argv)

window = QPushButton()
window.setWindowTitle("Moja aplikacja PyQt")
window.setGeometry(100, 100, 400, 300)

label = QLabel("Witaj w PyQt!", parent=window)
label.move(150, 130)

window.show()
sys.exit(app.exec())
\