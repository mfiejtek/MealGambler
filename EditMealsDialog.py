from PyQt6.QtWidgets import QDialog, QMessageBox, QListView
from PyQt6.QtGui import QStandardItem, QStandardItemModel
from PyQt6.QtCore import Qt, QModelIndex
from Ui_Files.Ui_EditMealsDialog import Ui_Dialog
from Meals_Database.meals_database_func import getAllMeals, deleteMeal, addMeal


class EditMealsDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Edit meals")  
        #List view ini  
        self.listView.setSelectionMode(QListView.SelectionMode.ExtendedSelection)
        self.listView.setModel(self.initializeListView())
        self.listView.setCurrentIndex(QModelIndex())
        #Buttons
        self.deleteButton.clicked.connect(self.deleteSelectedMeals)


    def initializeListView(self):
        meals = getAllMeals()
        model = QStandardItemModel()

        for meal in meals:
            name = meal[1]
            meal_item = QStandardItem(f"{name}")
            meal_item.setData(meal[0], Qt.ItemDataRole.UserRole)
            model.appendRow(meal_item)
        
        return model
    
    def deleteSelectedMeals(self):
        selected_indexes = self.listView.selectedIndexes()

        if selected_indexes:
            meal_ids = [index.data(Qt.ItemDataRole.UserRole) for index in selected_indexes]

            for meal_id in meal_ids:
                deleteMeal(meal_id)

            model = self.listView.model()
            for index in sorted(selected_indexes, key=lambda x: x.row(), reverse=True):
                model.removeRow(index.row())

            QMessageBox.information(self, "Deleted", "Marked meals have been removed")
        else:
            QMessageBox.warning(self, "Error", "Please mark meals for deletion.")

    


    


        