from PyQt6.QtWidgets import QDialog, QMessageBox

from Ui_Files.Ui_EditMealDialog import Ui_Dialog
from Meals_Database.meals_database_func import updateMeal


class EditMealDialog(QDialog, Ui_Dialog):
    def __init__(self, mealId, mealName, mealCategory, mealIngredients, parent = None,):
        super().__init__(parent)
        self.setupUi(self)

        self.setWindowTitle("Edit Meal")

        self.mealId = mealId
        self.nameLineEdit.setText(mealName)
        self.categoryComboBox.setCurrentText(mealCategory)

        self.ingredientsPlainTextEdit.setPlainText(mealIngredients)

        self.buttonBox.accepted.connect(self.saveChanges)

    def saveChanges(self):
        newName = self.nameLineEdit.text().strip()
        newCategory = self.categoryComboBox.currentText()
        newIngredients = self.ingredientsPlainTextEdit.toPlainText()

        if not newName:
            QMessageBox.warning(self, "Error", "Meal name cannot be empty.")
            return

        # Aktualizacja posiłku w bazie
        updateMeal(self.mealId, newName, newCategory, newIngredients)
        QMessageBox.information(self, "Success", "Meal updated successfully.")
        self.accept()


        