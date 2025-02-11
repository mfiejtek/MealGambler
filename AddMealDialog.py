from PyQt6.QtWidgets import QDialog, QMessageBox

from Ui_Files.Ui_EditMealDialog import Ui_Dialog
from Meals_Database.meals_database_func import addMeal

class AddMealDialog(QDialog, Ui_Dialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)

        self.setWindowTitle("Add Meal")

        # Pole do wpisania nazwy posiłku
        self.nameLineEdit.setPlaceholderText("Enter meal name...")
        self.ingredientsPlainTextEdit.setPlaceholderText("Enter list of ingredients...")
        self.buttonBox.accepted.connect(self.saveMeal)

    def saveMeal(self):
        mealName = self.nameLineEdit.text().strip()
        mealCategory = self.categoryComboBox.currentText()
        mealIngredients = self.ingredientsPlainTextEdit.toPlainText()

        if not mealName or not mealCategory or not mealIngredients:
            QMessageBox.warning(self, "Error", "Please input missing data.")
            return
        
        addMeal(mealName, mealCategory, mealIngredients)
        self.accept()