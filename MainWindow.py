import sys, os
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QSize
from Ui_Files.Ui_MainWindow import Ui_MainWindow
from Meals_Database.meals_database_func import initializeDatabase
from Meals_Database.user_settings_func import create_settings_file
from EditMealsDialog import EditMealsDialog
from GenerateMealsDialog import GenerateMealsDialog


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("MealGambler")
        self.setFixedSize(QSize(300, 150))

        self.centerWindow()

        self.editMealsButton.clicked.connect(self.openEditMealsDialog)
        self.generateButton.clicked.connect(self.openGenerateMealsDialog)
    
    def openGenerateMealsDialog(self):
        self.GenerateMealsDialog = GenerateMealsDialog(self)
        self.GenerateMealsDialog.exec()
    
    def openEditMealsDialog(self):
        self.EditMealsDialog = EditMealsDialog()
        self.EditMealsDialog.exec()

    def centerWindow(self):
        screen = QApplication.primaryScreen()
        screenGeometry = screen.availableGeometry()
        windowGeometry = self.frameGeometry()

        centerPoint = screenGeometry.center()
        windowGeometry.moveCenter(centerPoint)
        self.move(windowGeometry.topLeft())



if __name__ == "__main__":
    initializeDatabase()
    create_settings_file()
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(os.path.join(os.path.dirname(__file__), "icons", "icon.ico")))

    mainWindow = MainWindow()
    mainWindow.show()

    app.exec()