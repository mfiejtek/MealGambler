from PyQt6.QtWidgets import QDialog, QMessageBox, QListView
from PyQt6.QtGui import QStandardItem, QStandardItemModel
from PyQt6.QtCore import Qt, QModelIndex

from Ui_Files.Ui_EditMealsDialog import Ui_Dialog
from AddMealDialog import AddMealDialog
from EditMealDialog import EditMealDialog
from Meals_Database.meals_database_func import getAllMeals, deleteMeal


class EditMealsDialog(QDialog, Ui_Dialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Edit meals")  
        #List view ini  
        self.listView.setSelectionMode(QListView.SelectionMode.ExtendedSelection)
        self.mealsModel = QStandardItemModel()
        self.listView.setModel(self.mealsModel)
        self.loadMeals()
        self.listView.setCurrentIndex(QModelIndex())
        #Buttons
        self.deleteButton.clicked.connect(self.deleteSelectedMeals)
        self.addButton.clicked.connect(self.addNewMeal)
        self.editButton.clicked.connect(self.editMeal)


    def loadMeals(self):
        """Wczytuje posiłki z bazy i aktualizuje ListView"""
        self.mealsModel.clear()
        meals = getAllMeals()

        for meal in meals:
            mealItem = QStandardItem(meal[1])                           # Name
            mealItem.setData(meal[0], Qt.ItemDataRole.UserRole)         # Id
            mealItem.setData(meal[2], Qt.ItemDataRole.UserRole + 1)     # Category
            mealItem.setData(meal[3], Qt.ItemDataRole.UserRole + 2)     # Ingredients
            self.mealsModel.appendRow(mealItem)
        

    
    def deleteSelectedMeals(self):
        selectedIndexes = self.listView.selectedIndexes()

        if selectedIndexes:
            meal_ids = [index.data(Qt.ItemDataRole.UserRole) for index in selectedIndexes]

            for meal_id in meal_ids:
                deleteMeal(meal_id)

            model = self.listView.model()
            for index in sorted(selectedIndexes, key=lambda x: x.row(), reverse=True):
                model.removeRow(index.row())

            QMessageBox.information(self, "Deleted", "Marked meals have been removed")
        else:
            QMessageBox.warning(self, "Error", "Please mark meals for deletion.")



    def addNewMeal(self):
        dialog = AddMealDialog(self)
        if dialog.exec():
            self.loadMeals()
        QMessageBox.information(self, "Success", "Meal added successfully.")
        
    
    def editMeal(self):
        selectedIndexes = self.listView.selectedIndexes()

        if not selectedIndexes:
            QMessageBox.warning(self, "Error", "Please select a meal to edit.")
            return
        elif len(selectedIndexes) > 1:
            QMessageBox.warning(self, "Error", "Please select only ONE meal.")
            return

        index = selectedIndexes[0]
        mealId = index.data(Qt.ItemDataRole.UserRole)
        mealName = index.data(Qt.ItemDataRole.DisplayRole)  
        mealCategory = index.data(Qt.ItemDataRole.UserRole + 1)
        mealIngredients = index.data(Qt.ItemDataRole.UserRole + 2)

        dialog = EditMealDialog(mealId, mealName, mealCategory, mealIngredients, self)
        if dialog.exec():
            self.loadMeals()
        QMessageBox.information(self, "Success", "Meal updated successfully.")

    

    


    


        