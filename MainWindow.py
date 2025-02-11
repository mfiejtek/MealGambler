import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from Ui_Files.Ui_MainWindow import Ui_MainWindow
from Meals_Database.meals_database_func import initializeDatabase
from EditMealsDialog import EditMealsDialog

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("MealGambler")
        self.editMealsButton.clicked.connect(self.openEditMealsDialog)
    
    def openEditMealsDialog(self):
        self.EditMealsDialog = EditMealsDialog()
        self.EditMealsDialog.exec()


if __name__ == "__main__":
    initializeDatabase()
    app = QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()

    app.exec()