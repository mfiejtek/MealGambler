import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize
from Ui_Files.Ui_MainWindow import Ui_MainWindow
from Meals_Database.meals_database_func import initializeDatabase
from EditMealsDialog import EditMealsDialog
import os

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("MealGambler")
        self.setFixedSize(QSize(300, 150))
        self.setWindowIcon(QIcon("icon.png"))

        self.editMealsButton.clicked.connect(self.openEditMealsDialog)
    
    def openEditMealsDialog(self):
        self.EditMealsDialog = EditMealsDialog(self)
        self.EditMealsDialog.exec()


if __name__ == "__main__":
    initializeDatabase()
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.png"))

    mainWindow = MainWindow()
    mainWindow.show()

    app.exec()